# TCRMMT Super Admin Bilingual V1.14 — VERIFY

Target: `/var/www/TCRMMT`

Patch:
- `apply_superadmin_bilingual_v1_14.py`

Required baseline:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_13_OVERVIEW_MIXED_STATUS_CLOSURE`

V1.14 marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_14_COMPANIES_ACTION_COUNTER_CLOSURE`

Expected runtime:
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V114`
- `/super-admin/bilingual-v114.js`
- cache key `superadmin-bilingual-v114`

## Apply
1. Run `git status --short`.
2. Do not reset/clean/restore/commit/push.
3. Run the patch once.
4. Run it a second time; it must be no-op.
5. Only `server/superAdminUiPolish.ts` may be modified.

## Static checks
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

Before restart, `dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_14_COMPANIES_ACTION_COUNTER_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V114`
- `/super-admin/bilingual-v114.js`
- `superadmin-bilingual-v114`

## Restart
Restart only:
`pm2 restart tamiyouz-crm`

Confirm online and unstable restarts = 0.

## Asset proof
Direct Node and public HTTPS must return the V114 JS asset with:
- HTTP 200
- JavaScript Content-Type
- no-store headers
- marker `SUPER_ADMIN_BILINGUAL_RUNTIME_V114`

## Browser gates
Use a fresh browser context with cache disabled.

Reconfirm:
- default EN/LTR
- EN → AR → EN
- EN persistence
- AR persistence

Overview regression:
- `OVERVIEW EN STATIC UI: NONE FOUND`
- `OVERVIEW AR STATIC UI: NONE FOUND`

## Companies EN closure
After 2 seconds, these must be English:
- `N shown of N · page X/Y`
- `Copy Path`
- `Details`
- `Renew`
- `Login`
- `Risk`

Exclude only real company/user names, emails, IDs, URLs, paths/slugs, integration/product names, and raw technical identifiers.

Required:
`COMPANIES EN STATIC UI: NONE FOUND`

## Companies AR regression
Switch to Arabic and wait 2 seconds.

Expected localized equivalents:
- Arabic counter/page label
- Arabic Copy Path
- Arabic Details
- Arabic Renew
- Arabic Login
- Arabic Risk

Required:
`COMPANIES AR STATIC UI: NONE FOUND`

## Continue full audit
Only if all above pass, continue EN + AR audit:
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

Stop at the first ordinary untranslated static UI finding. Do not fix manually.

Final PASS requires:
- `RUNTIME V114: PASS`
- `LANGUAGE CONTROL LIFECYCLE: PASS`
- `PERSISTENCE: PASS`
- `OVERVIEW EN STATIC UI: NONE FOUND`
- `OVERVIEW AR STATIC UI: NONE FOUND`
- `COMPANIES EN STATIC UI: NONE FOUND`
- `COMPANIES AR STATIC UI: NONE FOUND`
- `UNTRANSLATED STATIC UI: NONE FOUND`
