# TCRMMT V1.45 — Evolution direct/hash loader fix

Target: `/var/www/TCRMMT`

## Scope
Functional runtime fix only. V1.44 bilingual runtime remains active.

Allowed tracked source changes after apply:
- `server/superAdminUiPolish.ts` — existing cumulative V1.44 bilingual changes
- `server/_core/index.ts` — V1.45 loader trigger fix

No other tracked files may change.

## Apply
Run `apply_superadmin_bilingual_v1_45.py` twice.
Expected:
1. `Applied Super Admin Evolution V1.45 direct/hash loader fix.`
2. `Super Admin Evolution V1.45 direct/hash loader fix already applied; no changes made.`

## Gates
- `git diff --check`
- `npm run check`
- `npm run build`
- confirm `SUPER_ADMIN_EVOLUTION_DIRECT_HASH_LOADER_V145` in source and `dist/index.js`

Restart only `tamiyouz-crm`, then stale-process guard: new PID start time must be after current `dist/index.js` mtime. Readiness on port 3002 within 90s.

## Primary browser gate
Fresh authenticated browser, cache disabled. Open a cache-busted direct URL ending in `#evolution-api`.

Without clicking Evolution nav or Refresh:
- `GET /api/super-admin/evolution-api/settings` must be sent automatically and return 200.
- page must leave `Not configured / Not saved / Checking...` initial state and render real settings/capability state.
- no duplicate uncontrolled request loop.

Then change hash away and back to `#evolution-api`; one loader cycle must occur and finish successfully.

## Resume bilingual QA
V1.44 runtime asset remains the expected translation runtime.
Verify Evolution API EN/AR V1.44 gates, then continue Full Audit:
Tara APIs → Plans Catalog → Plan Editor → Company Overrides → Commercial → Billing → Subscriptions → Settings → Source Code.

At first genuine ordinary untranslated static UI: STOP and capture exact text, selector/attribute, language/hash, screenshot. Exclude runtime/domain data and masked secret values.

No manual fix. No commit/push.

Create `TCRMMT_V145_Evidence.zip`.
