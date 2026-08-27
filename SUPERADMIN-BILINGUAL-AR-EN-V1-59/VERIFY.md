# TCRMMT Super Admin Bilingual V1.59 — VERIFY

## Purpose
V1.58 passed deployment/runtime and hard-closed all eight Commercial KPI labels. The first remaining genuine Commercial EN static blocker was the Global Safety Controls helper:

`أي تفعيل يحتاج تأكيدًا صريحًا. Kill Switch يعيد All companies إلى shadow.`

V1.59 hard-canonicalizes the fixed Global Safety Controls card by selector, preserving the actual form inputs and their runtime values.

## Patch
- target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`
- marker: `SUPER_ADMIN_BILINGUAL_AR_EN_V1_59_COMMERCIAL_SAFETY_CONTROLS_HARD_CLOSURE`
- runtime: `SUPER_ADMIN_BILINGUAL_RUNTIME_V159`
- asset: `/super-admin/bilingual-v159.js`
- cache key: `superadmin-bilingual-v159`

## Required EN
- `Global Safety Controls`
- `Any enablement requires explicit confirmation. Kill Switch returns all companies to shadow.`
- `Enable Enforcement`
- `Subscription Lifecycle Automation`
- `Automatic Invoice Generation`
- `Customer Portal`
- `Emergency Stop (Kill Switch)`
- `Canary %`
- `Currency`
- `Grace Days`
- `Save Safety Settings`

## Required AR
- `مفاتيح الأمان العامة`
- `أي تفعيل يحتاج تأكيدًا صريحًا. Kill Switch يعيد كل الشركات إلى shadow.`
- `تفعيل Enforcement`
- `دورة الاشتراك الآلية`
- `إنشاء الفواتير آليًا`
- `بوابة العميل`
- `مفتاح الإيقاف الطارئ (Kill Switch)`
- `نسبة Canary %`
- `العملة`
- `أيام السماح`
- `حفظ إعدادات الأمان`

## Preconditions
Production stays on `master`. Allowed cumulative tracked modified files only:
- `server/_core/index.ts`
- `server/superAdminUiPolish.ts`

Require V1.58 marker. No reset/clean/restore/manual edits.

## Apply
Run official V1.59 script twice.

Expected first:
`Applied Super Admin Bilingual V1.59 Commercial safety controls hard closure.`

Expected second:
`Super Admin bilingual V1.59 Commercial safety controls hard closure already applied; no changes made.`

## Gates
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All PASS. Confirm source/dist marker, V159 runtime, asset path/cache key.

Restart only `tamiyouz-crm` exactly once after all gates pass. New PM2 start epoch must be strictly greater than `dist/index.js` mtime. Port 3002 readiness <=90s.

## Runtime asset
Direct/Public `/super-admin/bilingual-v159.js?v=superadmin-bilingual-v159` 3x each:
- HTTP 200
- JavaScript content type
- `Cache-Control: no-store`
- V159 marker
- not HTML

## Browser primary
Fresh authenticated browser, cache disabled, read-only.

Carry forward already-proven non-Commercial regressions, then audit Commercial EN from the beginning. The old mixed helper is forbidden. Verify the complete Global Safety Controls card against the EN canonical list above without changing any control value.

Continue the full Commercial EN audit. Then natural AR and verify the same card against the AR list, followed by the full Commercial AR audit.

No Commercial mutation.

## Continue audit
After Commercial EN/AR PASS:
1. Billing EN
2. Billing AR
3. Subscriptions EN
4. Subscriptions AR
5. Settings EN
6. Settings AR
7. Source Code EN
8. Source Code AR

Stop at the first genuine ordinary untranslated static UI. Exclude agreed runtime/domain data. Do not fix manually.

## Evidence
Create exactly `TCRMMT_V159_Evidence.zip` and upload it plus Final Report to ChatGPT session exactly `TCRMMMT`.

No production commit/push.
