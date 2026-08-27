# TCRMMT Super Admin Bilingual V1.61 — VERIFY

## Purpose
V1.60 passed deployment/runtime and closed the Commercial tenant-editor fixed header. The first remaining genuine Commercial EN static blocker was the Plan Pricing label `السعر Minor` attached to `#priceAmount`.

V1.61 hard-canonicalizes the fixed Plan Pricing and Add-on Catalog form copy by selector. It does not modify any input value, selected option, plan/add-on identity, price, currency, status, invoice, metric or runtime/domain value.

## Patch
- target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`
- marker: `SUPER_ADMIN_BILINGUAL_AR_EN_V1_61_COMMERCIAL_MONETIZATION_FORMS_HARD_CLOSURE`
- runtime: `SUPER_ADMIN_BILINGUAL_RUNTIME_V161`
- asset: `/super-admin/bilingual-v161.js`
- cache key: `superadmin-bilingual-v161`

## Required EN — Plan Pricing
- `Plan Pricing`
- `Values are in minor currency units such as fils/cents.`
- `Plan`
- `Cycle`
- `Currency`
- `Price (minor units)`
- `Setup Fee (minor units)`
- `Price Active`
- `Save Price`

## Required AR — Plan Pricing
- `تسعير الباقات`
- `القيم بوحدة Minor مثل الفلس/السنت.`
- `الباقة`
- `الدورة`
- `العملة`
- `السعر بوحدة Minor`
- `رسوم التأسيس بوحدة Minor`
- `السعر نشط`
- `حفظ السعر`

## Required EN — Add-on Catalog
- `Add-on Catalog`
- `Features and limits as documented JSON.`
- `Slug`
- `Status`
- `Arabic Name`
- `English Name`
- `Cycle`
- `Currency`
- `Price (minor units)`
- `Feature Overrides JSON`
- `Limit Overrides JSON`
- `Save Add-on`

## Required AR — Add-on Catalog
- `كتالوج الإضافات`
- `الخصائص والحدود بصيغة JSON موثقة.`
- `المعرّف (Slug)`
- `الحالة`
- `الاسم العربي`
- `الاسم الإنجليزي`
- `الدورة`
- `العملة`
- `السعر بوحدة Minor`
- `استثناءات الخصائص JSON`
- `استثناءات الحدود JSON`
- `حفظ الإضافة`

## Safety
Production remains on `master`. Allowed cumulative tracked modified files only:
- `server/_core/index.ts`
- `server/superAdminUiPolish.ts`

V1.61 modifies only `server/superAdminUiPolish.ts`. Require V1.60 marker. No reset/clean/restore/manual edits.

## Apply
Run the official script twice.

Expected first:
`Applied Super Admin Bilingual V1.61 Commercial monetization forms hard closure.`

Expected second:
`Super Admin bilingual V1.61 Commercial monetization forms hard closure already applied; no changes made.`

## Gates
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All PASS. Confirm source/dist V1.61 marker, V161 runtime, asset path and cache key.

Restart only `tamiyouz-crm` exactly once after all gates pass. PM2 start epoch must be strictly newer than `dist/index.js` mtime. Port 3002 readiness <=90 seconds.

## Runtime asset
Direct/Public `/super-admin/bilingual-v161.js?v=superadmin-bilingual-v161` 3x each:
- HTTP 200
- JavaScript content type
- `Cache-Control: no-store`
- V161 marker
- not HTML

## Browser
Fresh authenticated browser, cache disabled, read-only.

Carry forward prior non-Commercial PASS results. Recheck Commercial EN from Plan Pricing onward. The old blocker `السعر Minor` is forbidden.

Plan Pricing and Add-on Catalog labels must match the canonical lists above. Inputs and selected values are runtime/domain data and must remain untouched.

Continue the complete Commercial EN audit. If PASS, switch naturally to AR and audit complete Commercial AR. Then continue Billing EN/AR, Subscriptions EN/AR, Settings EN/AR, Source Code EN/AR. Stop at the first genuine ordinary untranslated static UI.

No Commercial mutation. No production commit/push.

## Evidence
Create exactly `TCRMMT_V161_Evidence.zip` and upload it with Final Report to ChatGPT session exactly `TCRMMMT`.
