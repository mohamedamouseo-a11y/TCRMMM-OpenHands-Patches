# TCRMMT Super Admin Bilingual V1.47 — Tara APIs Full Static Closure

## Scope

Apply the official patch only to `/var/www/TCRMMT`.

Patch V1.47 changes only `server/superAdminUiPolish.ts`.
The cumulative production working tree is already expected to contain the authorized V1.45/V1.46 change in `server/_core/index.ts`, so after apply the only tracked modified files allowed are:

- `server/superAdminUiPolish.ts`
- `server/_core/index.ts`

Do not manually edit production source. Do not reset, clean, restore, commit, or push.

## Preflight

```bash
cd /var/www/TCRMMT
git status --short
grep -c 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_44_EVOLUTION_API_EN_RUNTIME_STATUS_HINTS_CLOSURE' server/superAdminUiPolish.ts
grep -c 'SUPER_ADMIN_EVOLUTION_DIRECT_HASH_RESTORE_V146' server/_core/index.ts
grep -c 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_47_TARA_APIS_FULL_STATIC_CLOSURE' server/superAdminUiPolish.ts
```

Required before first apply:

- V1.44 bilingual marker exists.
- V1.46 direct-hash marker exists.
- V1.47 marker does not yet exist.

## Apply twice

Use the official script from this folder:

```bash
python3 apply_superadmin_bilingual_v1_47.py
python3 apply_superadmin_bilingual_v1_47.py
```

Expected first output:

`Applied Super Admin Bilingual V1.47 Tara APIs full static closure runtime.`

Expected second output:

`Super Admin bilingual V1.47 Tara APIs full static closure already applied; no changes made.`

## Static gates

```bash
git status --short
git diff --check
npm run check
npm run build
```

All must pass.

Confirm `dist/index.js` contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_47_TARA_APIS_FULL_STATIC_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V147`
- `/super-admin/bilingual-v147.js`
- `superadmin-bilingual-v147`

No tracked file other than the cumulative authorized `server/superAdminUiPolish.ts` and `server/_core/index.ts` may be modified.

## Restart and stale-process guard

Restart only:

```bash
pm2 restart tamiyouz-crm
```

Prove the new PM2 process start time is strictly later than the current `dist/index.js` mtime. If stale, STOP.

Poll port 3002 for readiness for at most 90 seconds.

## Runtime asset V1.47

Test each URL three times:

- `http://127.0.0.1:3002/super-admin/bilingual-v147.js?v=superadmin-bilingual-v147`
- `https://tcrmmm.tamiyouz.com/super-admin/bilingual-v147.js?v=superadmin-bilingual-v147`

Each response must be:

- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V147`
- not HTML fallback

## V1.46 functional regression

Fresh authenticated browser, cache disabled.

Open directly with a cache-busted URL ending in:

`#evolution-api`

Do not first open Overview and do not click a mutating Evolution action.

Required after capabilities load:

- `location.hash === '#evolution-api'`
- active section = `sec-evolution-api`
- Evolution section visible
- one normal automatic `/api/super-admin/evolution-api/settings` load cycle
- no uncontrolled duplicate loop

Then navigate safely away to `#overview` and back to `#evolution-api`; require exactly one normal additional load cycle.

## Evolution regression EN/AR

Retain the V1.44 gates.

EN:
- `Configured and ready`
- saved hints begin `Saved: `
- managed capability canonical English
- secret placeholders = `Leave blank to keep the current value`
- `EVOLUTION API EN STATIC UI: NONE FOUND`

AR:
- `مُعد وجاهز`
- saved hints begin `محفوظ: `
- managed capability canonical Arabic
- enable label = `تفعيل تكامل Evolution API`
- secret placeholders = `اتركه فارغًا للاحتفاظ بالقيمة الحالية`
- `EVOLUTION API AR STATIC UI: NONE FOUND`

Never read secret values and never perform a mutating Evolution action.

## Tara APIs EN — PRIMARY V1.47 GATE

Open a fresh cache-busted page:

`/super-admin/tara-integrations?qa=v147-tara-en-<timestamp>`

Set/confirm:

- `lang=en`
- `dir=ltr`

Do not save, test, disable, delete, or mutate any integration.

The ordinary static surface must be English. At minimum verify:

- eyebrow = `Platform Administration · Tara`
- `h1` = `Tara Integrations`
- generic or selected-company subtitle is English while preserving the company name
- Back button = `Back to Admin Console`
- Bahgat link = `Bahgat Settings`
- Add buttons = `Add Integration`
- Company label = `Company`
- Reload = `Refresh Data`
- owner-only audit note is English
- stats labels/hints are English
- section heading = `Integrations and APIs`
- section help copy is English

If integration cards exist, verify ordinary card labels/status/actions are English while preserving provider names, tenant/company names, IDs, dates, and other domain/runtime values.

If there are no cards, verify the empty state is English.

Open the Add Integration modal only (opening is non-mutating). Do NOT submit it. Verify the modal's ordinary static labels/help/buttons/placeholders are English, including:

- `Add Integration`
- provider/status labels
- `Basic settings`
- `Connection data`
- API/model/credential field labels
- `Leave blank to keep the saved value`
- `Sensitive data is encrypted before storage.`
- `Save securely`
- `Close`

Close the modal without saving.

Expected:

`TARA APIs EN STATIC UI: NONE FOUND`

Forbidden ordinary Arabic static includes the V1.46 blocker set:

- `تكاملات تارا`
- `إدارة تكاملات الشركة المختارة بصورة آمنة، مع تشفير الأسرار وعدم عرضها بعد الحفظ.`
- `إدارة المنصة · تارا`
- `العودة إلى لوحة الإدارة`
- `إضافة تكامل`
- `متاح لمالك المنصة فقط. تُسجل جميع عمليات الحفظ والاختبار والتعطيل في سجل التدقيق.`

Do not flag Arabic company names or other domain data as static UI.

## Tara APIs AR reverse gate

Switch to Arabic using the normal allowed language mechanism.

Confirm:

- `lang=ar`
- `dir=rtl`
- `تكاملات تارا`
- `إدارة المنصة · تارا`
- `العودة إلى لوحة الإدارة`
- `إعدادات بهجت`
- `إضافة تكامل`
- Arabic control/stats/workspace labels
- Arabic empty/card labels if present
- Add Integration modal returns to canonical Arabic without saving

Expected:

`TARA APIs AR STATIC UI: NONE FOUND`

## Continue Full Audit

If Tara EN/AR passes, continue in this exact order:

1. Plans Catalog EN/AR
2. Plan Editor EN/AR
3. Company Overrides EN/AR
4. Commercial EN/AR
5. Billing EN/AR
6. Subscriptions EN/AR
7. Settings EN/AR
8. Source Code EN/AR

At the first genuine ordinary untranslated static UI: STOP immediately.

Do not manually fix it. Record:

- language
- page/hash
- exact text
- untranslated segment
- selector/attribute
- raw browser finding
- screenshot

Exclude runtime/domain data:

- names/company names
- emails
- IDs
- paths
- tenant/product/plan values
- roles
- dates/timestamps
- URLs/IPs
- repo/branch/SHA
- provider/product/brand names
- event payloads
- masked secret values
- raw technical errors

## Evidence

Create:

`TCRMMT_V147_Evidence.zip`

Include:

- preflight
- apply + no-op
- tracked scope
- static gates
- source/dist V1.47 markers
- PM2 restart + stale guard + readiness
- Direct/Public V1.47 runtime asset 3x
- V1.46 direct/hash regression
- Evolution EN/AR
- Tara EN full static gate
- Tara AR reverse gate
- modal read-only inspection
- Full Audit progress
- first genuine blocker if any
- screenshots
- final report

No commit. No push.

Upload the final report and `TCRMMT_V147_Evidence.zip` inside ChatGPT Session exactly named `TCRMMMT`.
