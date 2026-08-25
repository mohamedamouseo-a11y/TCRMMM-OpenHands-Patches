# TCRMMT Super Admin Bilingual V1.44 — Evolution API EN Runtime Status/Hints Closure

## Scope

Apply the official patch only to `/var/www/TCRMMT`.

Expected tracked production diff after apply:

- `server/superAdminUiPolish.ts` only

Do not manually edit production source. Do not reset, clean, restore, commit, or push.

## Preflight

```bash
cd /var/www/TCRMMT
git status --short
grep -c 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_43_EVOLUTION_API_AR_ENABLE_INTEGRATION_CANONICALIZATION' server/superAdminUiPolish.ts
grep -c 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_44_EVOLUTION_API_EN_RUNTIME_STATUS_HINTS_CLOSURE' server/superAdminUiPolish.ts
```

V1.43 prerequisite must exist. V1.44 must not already exist before first apply.

## Apply twice

```bash
python3 apply_superadmin_bilingual_v1_44.py
python3 apply_superadmin_bilingual_v1_44.py
```

Expected first output:

`Applied Super Admin Bilingual V1.44 Evolution API EN runtime status hints closure.`

Expected second output:

`Super Admin bilingual V1.44 Evolution API EN runtime status hints closure already applied; no changes made.`

## Static gates

```bash
git status --short
git diff --check
npm run check
npm run build
```

All must pass. Only `server/superAdminUiPolish.ts` may be tracked-modified.

Confirm `dist/index.js` contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_44_EVOLUTION_API_EN_RUNTIME_STATUS_HINTS_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V144`
- `/super-admin/bilingual-v144.js`
- `superadmin-bilingual-v144`

## Restart and stale guard

Restart only:

```bash
pm2 restart tamiyouz-crm
```

Prove the new PM2 process start time is strictly later than the current `dist/index.js` mtime. If stale, STOP.

Poll port 3002 for readiness for at most 90 seconds.

## Runtime asset

Check each URL three times:

- `http://127.0.0.1:3002/super-admin/bilingual-v144.js?v=superadmin-bilingual-v144`
- `https://tcrmmm.tamiyouz.com/super-admin/bilingual-v144.js?v=superadmin-bilingual-v144`

Each response must be HTTP 200, JavaScript Content-Type, `Cache-Control: no-store`, contain `SUPER_ADMIN_BILINGUAL_RUNTIME_V144`, and not be HTML fallback.

## Browser regressions

Fresh authenticated browser, cache disabled, cache-busted URL. EN then AR:

1. Users
2. Overview
3. Companies
4. Tenant Details
5. Platform Admins
6. Activity
7. Audit Log
8. GitHub Sync

Tenant Details may receive up to three clean rechecks if a transient skeleton appears. Do not patch/restart solely because of a transient first attempt.

## Evolution API EN — primary V1.44 gate

Open `#evolution-api` with `lang=en`, `dir=ltr`.

Do not click mutating actions. Do not read or modify secret input values.

Required:

- `#evolutionConnectionBadge` = `Configured and ready`
- `#evolutionApiTokenHint` starts with `Saved: ` and preserves the existing masked suffix exactly
- `#evolutionWebhookSecretHint` starts with `Saved: ` and preserves the existing masked suffix exactly
- `#evolutionManagedCapability` = `Automatic setup is available on the server. The service file will be updated and Evolution API restarted safely.`

Also retain all previous V1.40–V1.43 canonical English labels and both secret placeholders:

`Leave blank to keep the current value`

Expected:

`EVOLUTION API EN STATIC UI: NONE FOUND`

## Evolution API AR

Switch to `lang=ar`, `dir=rtl`.

Required:

- `#evolutionConnectionBadge` = `مُعد وجاهز`
- both saved hints begin with `محفوظ: ` while preserving the same masked suffix
- `#evolutionManagedCapability` = `الإعداد التلقائي متاح على السيرفر. سيتم تحديث ملف الخدمة وإعادة تشغيل Evolution API بأمان.`
- enable label = `تفعيل تكامل Evolution API`
- secret placeholders = `اتركه فارغًا للاحتفاظ بالقيمة الحالية`

Expected:

`EVOLUTION API AR STATIC UI: NONE FOUND`

## Continue Full Audit

If Evolution API EN/AR passes, continue EN then AR:

1. Tara APIs
2. Plans Catalog
3. Plan Editor
4. Company Overrides
5. Commercial
6. Billing
7. Subscriptions
8. Settings
9. Source Code

At the first genuine ordinary untranslated static UI: STOP. Do not fix. Record language, page/hash, exact text, untranslated segment, selector/attribute, raw browser finding, and screenshot.

Exclude runtime/domain data such as names, emails, IDs, paths, tenant/product/plan values, roles, dates/timestamps, URLs, IPs, repo/branch/SHA, event payloads, masked secret values, and raw technical errors.

## Evidence

Create `TCRMMT_V144_Evidence.zip` containing apply/no-op, scope, gates, markers, restart/stale proof, runtime checks, browser regressions, Evolution API EN/AR, Full Audit progress, first blocker if any, screenshots, and final report.

No commit. No push.

Upload the final report and `TCRMMT_V144_Evidence.zip` inside ChatGPT Session exactly named `TCRMMMT`.
