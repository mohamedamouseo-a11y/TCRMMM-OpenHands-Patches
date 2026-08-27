# TCRMMT Super Admin Bilingual V1.60 — VERIFY

## Purpose
V1.59 passed deployment/runtime, Commercial KPI labels, and Global Safety Controls EN. The first remaining genuine Commercial EN static blocker was the fixed tenant-editor subtitle:

`الDetails التجارية والتشغيلية الكاملة.`

V1.60 hard-canonicalizes the Commercial company-list and tenant-editor fixed header/default-state copy by selector. Dynamic tenant identity, status, plan, subscription and other runtime/domain values remain untouched.

## Patch
- target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`
- marker: `SUPER_ADMIN_BILINGUAL_AR_EN_V1_60_COMMERCIAL_TENANT_EDITOR_STATIC_HEADER_HARD_CLOSURE`
- runtime: `SUPER_ADMIN_BILINGUAL_RUNTIME_V160`
- asset: `/super-admin/bilingual-v160.js`
- cache key: `superadmin-bilingual-v160`

## Required EN fixed copy
- `Companies & Subscriptions`
- `Select a company to manage subscription, rollout, and usage.`
- `Search`
- placeholder `Company or plan`
- `Select a company`
- `Full commercial and operational details.`
- `Select a company from the list.`

## Required AR fixed copy
- `الشركات والاشتراكات`
- `اختر شركة لإدارة الاشتراك والتفعيل والاستهلاك.`
- `بحث`
- placeholder `الشركة أو الباقة`
- `اختر شركة`
- `التفاصيل التجارية والتشغيلية الكاملة.`
- `اختر شركة من القائمة.`

## Safety
Production remains on `master`. Allowed cumulative tracked modified files only:
- `server/_core/index.ts`
- `server/superAdminUiPolish.ts`

V1.60 modifies only `server/superAdminUiPolish.ts`. Require V1.59 marker. No reset/clean/restore/manual edits.

## Apply
Run the official script twice.

Expected first:
`Applied Super Admin Bilingual V1.60 Commercial tenant editor static header hard closure.`

Expected second:
`Super Admin bilingual V1.60 Commercial tenant editor static header hard closure already applied; no changes made.`

## Gates
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All PASS. Confirm source/dist V1.60 marker, V160 runtime, asset path and cache key.

Restart only `tamiyouz-crm` exactly once after all gates pass. PM2 start epoch must be strictly newer than `dist/index.js` mtime. Port 3002 readiness <=90 seconds.

## Runtime asset
Direct/Public `/super-admin/bilingual-v160.js?v=superadmin-bilingual-v160` 3x each:
- HTTP 200
- JavaScript content type
- `Cache-Control: no-store`
- V160 marker
- not HTML

## Browser
Fresh authenticated browser, cache disabled, read-only.

Carry forward prior non-Commercial PASS results. Recheck Commercial EN from the KPI/safety area onward. The old blocker `الDetails التجارية والتشغيلية الكاملة.` is forbidden. Verify the fixed list/editor copy above before and after selecting one existing company read-only.

Important: once a real company is selected, `#commercialTenantTitle`, `#commercialTenantSub`, badges, plan/status strings and other tenant data may become runtime/domain values; exclude those values from translation classification.

Continue the entire Commercial EN audit. If PASS, switch naturally to AR and audit Commercial AR. Then continue Billing EN/AR, Subscriptions EN/AR, Settings EN/AR, Source Code EN/AR. Stop at the first genuine ordinary untranslated static UI.

No Commercial mutation. No production commit/push.

## Evidence
Create exactly `TCRMMT_V160_Evidence.zip` and upload it with Final Report to ChatGPT session exactly `TCRMMMT`.
