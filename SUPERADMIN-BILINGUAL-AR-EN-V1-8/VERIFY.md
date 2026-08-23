# TCRMMT — Super Admin Bilingual V1.8 Standalone Runtime Verification

Target: `/var/www/TCRMMT`

Patch files:
- `apply_superadmin_bilingual_v1_8.py`
- `bilingual_runtime_v18.js`

Expected modified production file only:
- `server/superAdminUiPolish.ts`

## Safety
- Preserve the current worktree.
- Do not reset, clean, restore, commit, or push.
- Do not modify DB, Auth, APIs, Routes, Permissions, Billing, Subscription logic, or business logic.

## Apply
1. `git status --short`
2. Copy the V1.8 patch files outside the worktree.
3. Confirm `SUPER_ADMIN_BILINGUAL_AR_EN_V1_7_CACHE_BUST` exists in `server/superAdminUiPolish.ts`.
4. Run `node --check bilingual_runtime_v18.js` before patch application.
5. Run `python3 apply_superadmin_bilingual_v1_8.py` once.
6. Run it a second time; it must be a no-op.

## Static validation
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

Confirm only `server/superAdminUiPolish.ts` changed.
If PASS, restart only `tamiyouz-crm`.

## Asset proof — mandatory before browser QA
Fresh HTML must include all three versioned assets:
- `/super-admin/ui-polish-v2.css?v=superadmin-bilingual-v18`
- `/super-admin/ui-polish-v2.js?v=superadmin-bilingual-v18`
- `/super-admin/bilingual-v18.js?v=superadmin-bilingual-v18`

Fetch `/super-admin/bilingual-v18.js?v=superadmin-bilingual-v18` directly and prove:
- HTTP 200
- body contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V18`
- `Cache-Control: no-store, max-age=0, must-revalidate`
- `Pragma: no-cache`

Run a JS syntax check against the exact downloaded runtime body if possible (`node --check`).

## Browser runtime gate — fresh context only
Use a brand-new browser context with cache disabled.
Before interacting, console errors must be captured.

On Login with empty storage, after 2 seconds:
- `document.documentElement.dataset.saBilingualRuntime === 'SUPER_ADMIN_BILINGUAL_RUNTIME_V18'`
- `document.documentElement.dataset.saLang === 'en'`
- `document.documentElement.lang === 'en'`
- `document.documentElement.dir === 'ltr'`
- `localStorage['tcrm-super-admin-language'] === 'en'`
- visible login language button exists and displays `AR`
- title + aria-label = `Switch to Arabic`

If the runtime marker is absent, STOP and report browser console errors + network response for bilingual-v18.js. Do not continue translation QA.

## Lifecycle
Use only visible V1.8 language controls.
- EN -> AR: expect `ar/rtl`, localStorage `ar`, button `EN`, accessibility label `التبديل إلى الإنجليزية`
- AR -> EN: expect `en/ltr`, localStorage `en`, button `AR`, accessibility label `Switch to Arabic`

Persistence:
- EN -> refresh -> remains EN/LTR
- AR -> refresh -> remains AR/RTL

After login, verify controls in:
- authenticated topbar
- `.sa-ui-dock`

## Translation regression gate
After each render wait 2 seconds.
Scan visible text plus `placeholder`, `title`, and `aria-label`.

English must not contain ordinary static Arabic UI on:
- Overview
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
- Commercial / Billing / Subscriptions
- Settings / Source Code

Arabic must not contain ordinary static English UI, excluding real technical identifiers and business data.

Explicit regression checks:
- Arabic Overview: no `PLATFORM OVERVIEW`, `QUICK COMMANDS`, `ATTENTION`, `USAGE`, `GLOBAL SEARCH`, `SECURITY`, `ORGANIZATIONS`
- English Overview: no `متأخر / منتهي`, `كل الحسابات`, `نشاط المنصة`, `الإيراد الشهري`, `يتطلب متابعة`
- Arabic Plans: no `Back to Command Center`, `Refresh Data`, `View details`
- Arabic Commercial: no raw `Kill Switch`, `Canary %`, `Grace Days`, `Feature Overrides JSON`, `Limit Overrides JSON`

## Responsive
Both languages:
- 1440x900
- 1024x768
- 768x900
- 390x844

Expected horizontal overflow: 0px; no clipping/overlap.

## Final report gates
Report these exact lines:
- `STANDALONE RUNTIME ASSET: PASS/FAIL`
- `RUNTIME EXECUTION: PASS/FAIL`
- `LANGUAGE CONTROL LIFECYCLE: PASS/FAIL`
- `PERSISTENCE: PASS/FAIL`
- `UNTRANSLATED STATIC UI: NONE FOUND` or list every remaining finding with page, language, exact text, selector/attribute, screenshot.

Do not manually fix any finding. Return ZIP evidence and stop.
