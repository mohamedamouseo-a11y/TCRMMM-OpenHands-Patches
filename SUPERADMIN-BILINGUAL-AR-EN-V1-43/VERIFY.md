# TCRMMT Super Admin Bilingual V1.43 — Evolution API AR Enable Integration Canonicalization

## Patch scope

This patch must modify only:

`/var/www/TCRMMT/server/superAdminUiPolish.ts`

Required previous marker:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1_42_EVOLUTION_API_EN_SECRET_PLACEHOLDERS_CLOSURE`

New marker:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1_43_EVOLUTION_API_AR_ENABLE_INTEGRATION_CANONICALIZATION`

Runtime:

- `/super-admin/bilingual-v143.js`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V143`
- cache key `superadmin-bilingual-v143`

Evidence basis: V1.42 browser QA proved all prior regressions and Evolution API EN passed. The first genuine untranslated static AR blocker was:

`تفعيل Evolution API integration`

Expected:

`تفعيل تكامل Evolution API`

Selector:

`div.evolutionToggleRow > div > b`

This patch only pins this static label in the final Evolution API runtime sweep. It does not read or modify secret values.

## Apply

```bash
cd /var/www/TCRMMT
git status --short
python3 /path/to/SUPERADMIN-BILINGUAL-AR-EN-V1-43/apply_superadmin_bilingual_v1_43.py
python3 /path/to/SUPERADMIN-BILINGUAL-AR-EN-V1-43/apply_superadmin_bilingual_v1_43.py
```

First run must print:

`Applied Super Admin Bilingual V1.43 Evolution API AR enable-integration canonicalization runtime.`

Second run must print:

`Super Admin bilingual V1.43 Evolution API AR enable-integration canonicalization already applied; no changes made.`

No manual edits.

Only tracked modified file allowed:

`server/superAdminUiPolish.ts`

## Static gates

```bash
git diff --check
npm run check
npm run build
```

All must PASS.

Verify built output contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_43_EVOLUTION_API_AR_ENABLE_INTEGRATION_CANONICALIZATION`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V143`
- `/super-admin/bilingual-v143.js`
- `superadmin-bilingual-v143`

## PM2 stale-process guard

Only after all static gates pass:

```bash
pm2 restart tamiyouz-crm
```

Restart only `tamiyouz-crm`.

Prove the new process start time is strictly later than the current `dist/index.js` mtime. If not, STOP.

Poll port 3002 for at most 90 seconds.

## Runtime asset gate

Test each 3 times:

Direct:

`http://127.0.0.1:3002/super-admin/bilingual-v143.js?v=superadmin-bilingual-v143`

Public:

`https://tcrmmm.tamiyouz.com/super-admin/bilingual-v143.js?v=superadmin-bilingual-v143`

Each must have:

- HTTP 200
- JavaScript Content-Type
- Cache-Control no-store
- V143 runtime marker
- no HTML fallback

## Browser regressions

Use a fresh authenticated browser, cache disabled, cache-busted URL.

Run EN then AR:

1. Users
2. Overview
3. Companies
4. Tenant Details
5. Platform Admins
6. Activity
7. Audit Log
8. GitHub Sync

For Tenant Details, if a first attempt shows the known transient skeleton, perform up to 3 clean rechecks before classifying failure. Do not patch or restart for a first transient attempt.

Keep every prior bilingual regression gate.

## Evolution API EN

Open `#evolution-api`.

Require:

- `lang=en`
- `dir=ltr`

The target selector:

`div.evolutionToggleRow > div > b`

must equal exactly:

`Enable Evolution API integration`

The V1.42 secret placeholders must remain exactly:

`Leave blank to keep the current value`

for:

- `#evolutionApiToken`
- `#evolutionWebhookSecret`

Do not read or modify secret field values.

All V1.40/V1.41 Evolution API English static strings must remain canonical.

Expected:

`EVOLUTION API EN STATIC UI: NONE FOUND`

## Evolution API AR — primary V1.43 gate

Switch to Arabic:

- `lang=ar`
- `dir=rtl`

The target selector:

`div.evolutionToggleRow > div > b`

must equal exactly:

`تفعيل تكامل Evolution API`

Forbidden:

`تفعيل Evolution API integration`

Secret placeholders must remain exactly:

`اتركه فارغًا للاحتفاظ بالقيمة الحالية`

Expected:

`EVOLUTION API AR STATIC UI: NONE FOUND`

## Continue Full Audit

Only if Evolution API EN/AR PASS, continue EN then AR:

1. Tara APIs
2. Plans Catalog
3. Plan Editor
4. Company Overrides
5. Commercial
6. Billing
7. Subscriptions
8. Settings
9. Source Code

At the first genuine ordinary untranslated static UI, STOP immediately.

Do not manually fix, reset, clean, restore, commit, or push.

Capture:

- language
- page/hash
- exact text
- untranslated segment
- selector/attribute
- raw browser finding
- screenshot

Exclude runtime/domain data such as names, company names, emails, dates/timestamps, IDs, paths, tenant/product/plan values, roles, URLs, IPs, repository/branch/SHA, event payloads, operational statuses, and raw technical errors.

## Evidence package

Create:

`TCRMMT_V143_Evidence.zip`

Include:

- apply/no-op evidence
- git status/scope
- static gates
- built markers
- PM2 restart and stale guard proof
- readiness
- Direct/Public runtime asset checks
- browser regressions
- Evolution API EN/AR
- Full Audit progress
- first genuine blocker if any
- screenshots
- final report

No commit. No push.

Upload final report and Evidence ZIP into ChatGPT Session named exactly:

`TCRMMMT`
