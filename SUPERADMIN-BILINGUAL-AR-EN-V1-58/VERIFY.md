# TCRMMT Super Admin Bilingual V1.58 — VERIFY

## Purpose
V1.57 deployment/runtime passed and its Commercial subtitle/full closure worked, but Commercial EN stopped at the first genuine remaining static blocker: `طلبات Pending` in `#commercialSummary .summaryCard:nth-child(7) > span`. The value sibling is runtime data; the label is ordinary static UI.

V1.58 hard-canonicalizes only the eight static Commercial Summary KPI label spans by their fixed schema order. It never changes the KPI `<b>` values or company/subscription/billing domain data.

## Patch
- target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`
- marker: `SUPER_ADMIN_BILINGUAL_AR_EN_V1_58_COMMERCIAL_KPI_SUMMARY_HARD_CLOSURE`
- runtime: `SUPER_ADMIN_BILINGUAL_RUNTIME_V158`
- asset: `/super-admin/bilingual-v158.js`
- cache key: `superadmin-bilingual-v158`

## Required KPI labels
EN:
1. Active Subscriptions
2. At-risk Subscriptions
3. Overdue Invoices
4. Total Open Invoices
5. Enabled Companies
6. Usage Alerts
7. Pending Requests
8. Kill Switch

AR:
1. اشتراكات نشطة
2. اشتراكات معرضة
3. فواتير متأخرة
4. إجمالي الفواتير المفتوحة
5. شركات مفعلة
6. تنبيهات استخدام
7. طلبات معلقة
8. مفتاح الإيقاف

The numeric/text KPI values in sibling `<b>` elements are excluded runtime/domain data and must not be changed/read beyond what is necessary to confirm the labels are separate.

## Preconditions
Production stays on `master`. Allowed cumulative tracked modified files only: `server/_core/index.ts` and `server/superAdminUiPolish.ts`. Require V1.57 marker. No reset/clean/restore/manual edits.

## Apply
Run official V1.58 script twice. Expected first: `Applied Super Admin Bilingual V1.58 Commercial KPI summary hard closure.` Expected second: `Super Admin bilingual V1.58 Commercial KPI summary hard closure already applied; no changes made.`

## Gates
`git diff --check`, `npm run check`, `npm run build` all PASS. Confirm source/dist marker, V158 runtime, asset path/cache key. Restart only `tamiyouz-crm` exactly once after gates. New PM2 start epoch > `dist/index.js` mtime; readiness <=90s.

## Asset
Direct/Public `/super-admin/bilingual-v158.js?v=superadmin-bilingual-v158` 3x each: HTTP 200, JavaScript content type, no-store, V158 marker, not HTML.

## Browser primary
Fresh authenticated browser, cache disabled, read-only. Regress prior V1.57 PASS areas, then Commercial EN. The old exact blocker `طلبات Pending` is forbidden. All eight KPI labels must match the EN list above. Continue the entire Commercial EN audit; then natural AR and verify all eight AR labels. Stop only on the first genuine ordinary static blocker. Exclude agreed runtime/domain data.

## Continue audit
After Commercial EN/AR PASS: Billing EN/AR, Subscriptions EN/AR, Settings EN/AR, Source Code EN/AR. Stop at first genuine static blocker. No production commit/push.

## Evidence
Create `TCRMMT_V158_Evidence.zip` and upload it plus Final Report to ChatGPT session exactly `TCRMMMT`.
