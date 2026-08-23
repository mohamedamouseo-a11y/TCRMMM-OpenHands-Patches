# Super Admin Bilingual AR/EN V1.7 — Asset Cache-Bust Runtime Fix

## Purpose
V1.6 is present in source/build, but browser evidence showed no language controls and stale untranslated UI. The Super Admin CSS/JS assets are served from stable URLs with `Cache-Control: public, max-age=3600`, so browsers/test contexts can keep executing an older asset even after rebuild/restart.

V1.7 does **not** add another translation dictionary. It makes the already-applied V1–V1.6 runtime reliably reach the browser by:

- bumping `UI_VERSION` and runtime `VERSION` to `SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V17`;
- adding `?v=superadmin-bilingual-v17` cache-busters to injected CSS and JS asset URLs;
- changing Super Admin polish asset responses to `Cache-Control: no-store, max-age=0, must-revalidate` and `Pragma: no-cache`.

## Target
`/var/www/TCRMMT/server/superAdminUiPolish.ts`

## Apply

```bash
python3 apply_superadmin_bilingual_v1_7.py
```

Run again and confirm no-op.

## Static checks

```bash
git diff --check
npm run check
npm run build
```

Only `server/superAdminUiPolish.ts` may change.

## Restart
Restart only `tamiyouz-crm`.

## Mandatory asset proof BEFORE UI QA
Fetch a fresh Super Admin HTML response and prove it contains both cache-busted asset URLs:

- `/super-admin/ui-polish-v2.css?v=superadmin-bilingual-v17`
- `/super-admin/ui-polish-v2.js?v=superadmin-bilingual-v17`

Then fetch the JS asset URL directly and prove the response body contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_6`
- `SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V17`

Also prove JS response headers contain:

- `Cache-Control: no-store, max-age=0, must-revalidate`

If any of these asset proofs fail, STOP and report the response headers/body evidence. Do not continue UI QA.

## Browser QA requirements
Use a brand-new browser context with cache disabled or a fresh incognito context. Do not reuse the V1.6 context.

Before login verify:

- language button is visible;
- default state is `en/ltr` when no storage value exists;
- button shows `AR` in English;
- clicking switches to `ar/rtl` and button becomes `EN`;
- localStorage key `tcrm-super-admin-language` is written.

After login verify language controls exist in:

1. authenticated topbar;
2. `.sa-ui-dock`;

Perform EN → AR → EN using visible controls only. After each switch wait 2 seconds and record:

- `document.documentElement.lang`;
- `document.documentElement.dir`;
- `document.documentElement.dataset.saLang`;
- localStorage language value;
- visible button text/title/aria-label.

Persistence:

- select EN, refresh, confirm EN/LTR;
- select AR, refresh, confirm AR/RTL.

## Translation regression gate
Only after asset proof and lifecycle PASS, repeat the V1.6 translation audit.

Arabic Overview must not contain:

- `PLATFORM OVERVIEW`
- `QUICK COMMANDS`
- `ATTENTION`
- `USAGE`
- `GLOBAL SEARCH`
- `SECURITY`
- `ORGANIZATIONS`
- `إنشاء Workspace جديد`
- `حفظ Admin وصلاحيات الشركات`

English Overview must not contain:

- `متأخر / منتهي`
- `كل الحسابات`
- `نشاط المنصة`
- `الإيراد الشهري`
- `يتطلب متابعة`

Then continue the full V1.6 page matrix if those gates pass.

## Acceptance
Final report must include:

- `ASSET CACHE BUST: PASS`
- `LANGUAGE CONTROL LIFECYCLE: PASS`
- `PERSISTENCE: PASS`
- `UNTRANSLATED STATIC UI: NONE FOUND`

No commit or push from the target project.
