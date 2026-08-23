# Super Admin Bilingual V1.9 — Compatibility Runner Verification

Use this only after the original V1.9 patch stopped with:

`V1.9 dictionary injection anchor count is 0; refusing unknown baseline.`

## Safety
- Do not reset, clean, restore, commit, or push.
- Do not manually edit `server/superAdminUiPolish.ts`.
- The original failed V1.9 attempt must have left the target unchanged.

## Preconditions
1. `server/superAdminUiPolish.ts` contains `SUPER_ADMIN_BILINGUAL_AR_EN_V1_8_STANDALONE_RUNTIME`.
2. `server/superAdminUiPolish.ts` does NOT contain `SUPER_ADMIN_BILINGUAL_AR_EN_V1_9_PHRASE_RUNTIME` before applying.
3. Both patch files are present together:
   - `apply_superadmin_bilingual_v1_9.py`
   - `apply_superadmin_bilingual_v1_9_compat.py`

## Apply
Run:

`python3 apply_superadmin_bilingual_v1_9_compat.py`

Expected: original V1.9 patch applies successfully through a temporary corrected copy.

Run the same command a second time. Expected: V1.9 reports already applied / no changes.

## Static gates
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

The only source file modified by this patch must be:
`server/superAdminUiPolish.ts`

Before restart, verify `dist/index.js` contains:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_9_PHRASE_RUNTIME`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V19`
- `/super-admin/bilingual-v19.js`
- `superadmin-bilingual-v19`

If any marker is missing, stop and do not restart.

## Restart
If all static gates pass, restart only:
`pm2 restart tamiyouz-crm`

## Runtime + translation gates
Use a fresh browser context with cache disabled.

Required:
- V19 asset returns HTTP 200 JavaScript.
- `dataset.saBilingualRuntime = SUPER_ADMIN_BILINGUAL_RUNTIME_V19`.
- EN/AR toggle works both ways.
- Persistence works after refresh in both languages.

Check Overview EN first after waiting 2 seconds after render. If any ordinary Arabic static UI remains, stop and report UNIQUE strings with page, selector/attribute, and screenshot. Do not fix.

If Overview EN passes, continue full EN+AR audit across Login, Overview, Companies, Tenant Details, Users, Platform Admins, Activity, Audit Log, GitHub Sync, Evolution API, Tara APIs, Plans Catalog, Plan Editor, Company Overrides, Commercial, Billing, Subscriptions, Settings, and Source Code.

Final acceptance requires:
- `RUNTIME V19: PASS`
- `LANGUAGE CONTROL LIFECYCLE: PASS`
- `PERSISTENCE: PASS`
- `UNTRANSLATED STATIC UI: NONE FOUND`
