# Super Admin Bilingual V1.11 — Overview AR Closure Verification

Target: `/var/www/TCRMMT`

## Rules
- No reset / clean / restore.
- No commit / push.
- No manual code edits.
- Only `server/superAdminUiPolish.ts` may change.
- Require V1.10 marker before apply.

## Apply
1. `git status --short`
2. Confirm `SUPER_ADMIN_BILINGUAL_AR_EN_V1_10_OVERVIEW_CLOSURE` exists.
3. Run `python3 apply_superadmin_bilingual_v1_11.py` once.
4. Run it again; second run must be no-op.
5. `git diff --check`
6. `npm run check`
7. `npm run build`

## Dist Gate
Before restart, `dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_11_OVERVIEW_AR_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V111`
- `/super-admin/bilingual-v111.js`
- `superadmin-bilingual-v111`

If any marker is missing, stop.

## Restart
Restart only `tamiyouz-crm` after all gates pass. Confirm online and unstable restarts = 0.

## Runtime Asset
Direct Node and public HTTPS asset must return JavaScript 200 with marker `SUPER_ADMIN_BILINGUAL_RUNTIME_V111` and no-store cache headers.

## Browser Gate
Fresh context + cache disabled. Confirm:
- runtime V111
- EN/LTR default
- EN → AR → EN
- EN persistence after refresh
- AR persistence after refresh
- Login/topbar/dock language controls present

## Overview Regression
### English
Re-run the exact V1.10 Overview EN scan after 2 seconds. Required: `uniqueCount: 0` for ordinary Arabic static UI.

### Arabic
Re-run Overview AR after 2 seconds. The following must no longer appear as ordinary static/mixed UI:
- `Organizations`
- `Users & Access`
- `Plans & Commercial`
- `Platform Administration`
- `Tenant ID`
- `إضافة Admin`
- `حفظ Admin وصلاحيات الشركات`
- `استخدم Ctrl/Cmd لاختيار أكثر من شركة`

Dynamic patterns must render in Arabic:
- `Health N% · expired` → Arabic equivalent
- `N active of N` → Arabic equivalent
- `N paid companies` → Arabic equivalent
- `N suspended · N ending soon` → Arabic equivalent

Allowed exclusions remain real names/data, emails, IDs, URLs, product/integration names, technical identifiers, currency codes, language-control `EN`, and sample placeholders.

## Full Audit
Only if Overview EN and AR both pass, continue full EN + AR audit across Login, Companies, Tenant Details, Users, Platform Admins, Activity, Audit, GitHub, Evolution API, Tara APIs, Plans, Plan Editor, Overrides, Commercial/Billing/Subscriptions, Settings, and Source Code.

## Responsive
EN + AR at 1440×900, 1024×768, 768×900, 390×844. Require zero horizontal overflow, no clipping, no overlap.

## Acceptance
Final report must contain:
- `RUNTIME V111: PASS`
- `LANGUAGE CONTROL LIFECYCLE: PASS`
- `PERSISTENCE: PASS`
- `OVERVIEW EN STATIC UI: NONE FOUND`
- `OVERVIEW AR STATIC UI: NONE FOUND`
- `UNTRANSLATED STATIC UI: NONE FOUND`

If any static UI finding remains, do not fix it. Report exact text, language, page, selector/attribute, screenshot, and stop.
