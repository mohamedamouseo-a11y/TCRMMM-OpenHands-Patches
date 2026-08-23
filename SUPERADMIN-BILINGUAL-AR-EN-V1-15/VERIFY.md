# Super Admin Bilingual V1.15 — Verification

Target: `/var/www/TCRMMT`

Purpose: close only the two mixed Companies AR counter/pager findings from V1.14 evidence while preserving Overview EN/AR and Companies EN.

## Preconditions

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_14_COMPANIES_ACTION_COUNTER_CLOSURE` exists.
- V1.15 marker does not exist before first apply.
- Do not use reset/clean/restore/commit/push/manual edits.

## Apply

Run `python3 apply_superadmin_bilingual_v1_15.py` twice. Second run must be no-op.

Only `server/superAdminUiPolish.ts` may be modified.

## Static checks

Run:

- `git diff --check`
- `npm run check`
- `npm run build`

Before restart, `dist/index.js` must contain:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_15_COMPANIES_AR_COUNTER_PAGER_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V115`
- `/super-admin/bilingual-v115.js`
- `superadmin-bilingual-v115`

## Restart

Restart only `tamiyouz-crm` and verify online / unstable restarts 0.

## Runtime asset

Direct Node + Public endpoint:

`/super-admin/bilingual-v115.js?v=superadmin-bilingual-v115`

Must be HTTP 200 JavaScript, V115 marker present, no-store headers.

## Browser gates

Use fresh context, cache disabled. Verify lifecycle and persistence.

### Overview regression

Both must remain:

- `OVERVIEW EN STATIC UI: NONE FOUND`
- `OVERVIEW AR STATIC UI: NONE FOUND`

### Companies EN regression

Must remain:

- `COMPANIES EN STATIC UI: NONE FOUND`

Expected examples: `N shown of N · page X/Y`, `Copy Path`, `Details`, `Renew`, `Login`, `Risk`.

### Companies AR closure

The previous V1.14 findings must be gone.

Forbidden exact/mixed forms:

- `N معروضة من أصل N · page X/Y`
- `ترقيم صفحات من الخادم · N records`

Expected Arabic forms:

- `N معروضة من أصل N · صفحة X/Y`
- `ترقيم صفحات من الخادم · N سجل`

Actions must remain Arabic: `نسخ المسار`, `تفاصيل`, `تجديد`, `دخول`, `خطر`.

Acceptance:

- `COMPANIES AR STATIC UI: NONE FOUND`

## Full audit

If Companies EN+AR pass, continue EN+AR:

Tenant Details, Users, Platform Admins, Activity, Audit Log, GitHub Sync, Evolution API, Tara APIs, Plans Catalog, Plan Editor, Company Overrides, Commercial, Billing, Subscriptions, Settings, Source Code.

Stop at first ordinary untranslated static UI. Do not fix manually.

## Final acceptance strings

- `RUNTIME V115: PASS`
- `LANGUAGE CONTROL LIFECYCLE: PASS`
- `PERSISTENCE: PASS`
- `OVERVIEW EN STATIC UI: NONE FOUND`
- `OVERVIEW AR STATIC UI: NONE FOUND`
- `COMPANIES EN STATIC UI: NONE FOUND`
- `COMPANIES AR STATIC UI: NONE FOUND`
- `UNTRANSLATED STATIC UI: NONE FOUND`

If any gate fails, capture exact text, page, language, selector/attribute, screenshot, and stop. No commit or push.
