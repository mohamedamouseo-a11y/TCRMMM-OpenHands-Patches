# TCRMMT Super Admin Bilingual V1.42 — VERIFY

## Scope

Patch V1.42 closes the two evidence-backed Evolution API English-mode secret-field placeholders only.

Target tracked source:
`/var/www/TCRMMT/server/superAdminUiPolish.ts`

Required previous marker:
`SUPER_ADMIN_BILINGUAL_AR_EN_V1_41_EVOLUTION_API_EN_REMAINING_STATIC_CLOSURE`

New marker:
`SUPER_ADMIN_BILINGUAL_AR_EN_V1_42_EVOLUTION_API_EN_SECRET_PLACEHOLDERS_CLOSURE`

Runtime:
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V142`
- `/super-admin/bilingual-v142.js`
- `superadmin-bilingual-v142`

## Apply

From `/var/www/TCRMMT` run the official script twice.

Expected first output:
`Applied Super Admin Bilingual V1.42 Evolution API EN secret placeholders closure runtime.`

Expected second output:
`Super Admin bilingual V1.42 Evolution API EN secret placeholders closure already applied; no changes made.`

No manual edits.

Only tracked modified file may be:
`server/superAdminUiPolish.ts`

## Static gates

Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

Confirm dist contains:
- V1.42 marker
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V142`
- `/super-admin/bilingual-v142.js`
- `superadmin-bilingual-v142`

## Restart / stale guard

Restart only:
`pm2 restart tamiyouz-crm`

Prove the new PM2 process start time is AFTER current `dist/index.js` mtime.
If stale, STOP.

Poll port 3002 for readiness, maximum 90 seconds.

## Runtime asset gate

Test each 3 times:

Direct:
`http://127.0.0.1:3002/super-admin/bilingual-v142.js?v=superadmin-bilingual-v142`

Public:
`https://tcrmmm.tamiyouz.com/super-admin/bilingual-v142.js?v=superadmin-bilingual-v142`

Require:
- HTTP 200
- JavaScript Content-Type
- Cache-Control no-store
- V142 runtime marker
- no HTML fallback

## Browser regression gates

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

For Tenant Details, a first-attempt skeleton is not itself a translation blocker. Recheck cleanly up to 3 attempts. Do not patch/restart merely for a transient attempt.

Retain all previous canonical gates, including:
- Users EN `<runtime-count> accounts`; AR `<runtime-count> حساب`
- Audit canonical options
- GitHub cleanup EN `Safe Cleanup`; AR `إلغاء آمن`

## Evolution API EN — primary V1.42 gate

Open `#evolution-api`.

Require:
- `lang=en`
- `dir=ltr`

Do not enter, expose, save, generate, rotate, test, or otherwise mutate credentials.

Selectors / attribute:
- `#evolutionApiToken` → `placeholder`
- `#evolutionWebhookSecret` → `placeholder`

Both must equal exactly:
`Leave blank to keep the current value`

Forbidden:
`اتركه فارغًا للاحتفاظ بالقيمة الحالية`

Also verify all V1.40/V1.41 Evolution API English static strings remain canonical.

Expected:
`EVOLUTION API EN STATIC UI: NONE FOUND`

## Evolution API AR

Switch to Arabic:
- `lang=ar`
- `dir=rtl`

Both placeholders must equal exactly:
`اتركه فارغًا للاحتفاظ بالقيمة الحالية`

Expected:
`EVOLUTION API AR STATIC UI: NONE FOUND`

The patch changes placeholder attributes only. It must not read or modify secret field values.

## Continue Full Audit

If Evolution API EN/AR PASS, continue EN then AR:
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

Capture:
- language
- page/hash
- exact text
- untranslated segment
- selector/attribute
- raw browser finding
- screenshot

Exclude runtime/domain data such as names, emails, IDs, timestamps, paths, tenant/product/plan values, roles, URLs, IPs, repository/branch/SHA, event payloads, operational statuses, and raw technical errors.

Do not manually fix, reset, clean, restore, commit, or push.

## Evidence

Create:
`TCRMMT_V142_Evidence.zip`

Include:
- apply/no-op
- tracked scope
- diff/check/build
- dist markers
- restart + stale guard
- readiness
- Direct/Public runtime asset 3x
- regression results
- Evolution API EN/AR
- Full Audit progress
- first blocker if any
- screenshots
- final report

NO COMMIT.
NO PUSH.

Upload final report and Evidence ZIP inside ChatGPT Session exactly:
`TCRMMMT`
