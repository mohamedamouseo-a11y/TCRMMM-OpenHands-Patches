# TCRMMT Super Admin Bilingual V1.57 — VERIFY

## Purpose
V1.56 evidence passed Evolution EN/AR, Tara EN/AR, Plans Catalog/Editor EN/AR, query precedence, and Company Overrides EN/AR. The first genuine remaining ordinary static blocker is Commercial EN subtitle:

`متابعة التفعيل والاستهلاك ودورة الاشتراك والفواتير بمؤشرات قابلة للتنفيذ.`

V1.57 adds a page-scoped Commercial Operations closure for ordinary static and safe dynamic UI copy. It does not modify subscription, billing, plan, invoice, add-on, tenant, or runtime data/business logic.

## Patch
- target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`
- marker: `SUPER_ADMIN_BILINGUAL_AR_EN_V1_57_COMMERCIAL_FULL_STATIC_DYNAMIC_CLOSURE`
- runtime: `SUPER_ADMIN_BILINGUAL_RUNTIME_V157`
- asset: `/super-admin/bilingual-v157.js`
- cache key: `superadmin-bilingual-v157`

## Preconditions
Production remains on `master`.
Allowed cumulative tracked modified files only:
- `server/_core/index.ts`
- `server/superAdminUiPolish.ts`

Require V1.56 marker:
`SUPER_ADMIN_BILINGUAL_AR_EN_V1_56_EVOLUTION_CREDENTIALS_STATUS_LABELS_CLOSURE`

No reset/clean/restore. No manual edits.

## Apply
Run official V1.57 script twice.

First output exactly:
`Applied Super Admin Bilingual V1.57 Commercial full static/dynamic closure.`

Second output exactly:
`Super Admin bilingual V1.57 Commercial full static/dynamic closure already applied; no changes made.`

## Gates
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All PASS.

Confirm source/dist marker, V157 runtime, asset path, and cache key.

Restart only `tamiyouz-crm` exactly once after all gates pass.
New PM2 start epoch must be strictly greater than `dist/index.js` mtime.
Port 3002 readiness <=90s.

## Runtime asset
Direct/Public `/super-admin/bilingual-v157.js?v=superadmin-bilingual-v157` three times each:
- HTTP 200
- JavaScript content type
- Cache-Control no-store
- V157 marker
- not HTML

## Browser
Fresh authenticated browser, cache disabled, read-only.

Regression:
- Evolution EN/AR PASS
- Tara EN/AR PASS
- Plans Catalog/Editor EN/AR PASS
- Query precedence PASS
- Company Overrides EN/AR PASS

Primary Commercial EN:
- open Plans naturally in EN
- open Commercial (`commercialTab`)
- `lang=en`, `dir=ltr`, `data-sa-lang=en`
- forbidden subtitle:
  `متابعة التفعيل والاستهلاك ودورة الاشتراك والفواتير بمؤشرات قابلة للتنفيذ.`
- required subtitle:
  `Track rollout, usage, subscription lifecycle, and billing with actionable indicators.`
- audit full ordinary static Commercial surface
- may select one existing company read-only to reveal editor
- no Save/Reconcile/Rollback/Generate/Pay/Acknowledge/Approve/Reject or field persistence

Commercial AR:
- natural AR handoff
- `lang=ar`, `dir=rtl`, `data-sa-lang=ar`
- required subtitle:
  `متابعة التفعيل والاستهلاك ودورة الاشتراك والفواتير بمؤشرات قابلة للتنفيذ.`
- audit full ordinary static surface read-only

Exclude domain/runtime values:
company names, emails, IDs, dates/timestamps, URLs/IPs, plan/add-on names/slugs/versions, invoice numbers, amounts/currencies, subscription/rollout status values, metrics, counts, feature/limit catalog values, runtime values, raw technical errors, repo/branch/SHA, secrets.

After Commercial EN/AR PASS continue:
1. Billing EN/AR
2. Subscriptions EN/AR
3. Settings EN/AR
4. Source Code EN/AR

Stop at first genuine ordinary untranslated static UI. Do not fix it.

## Evidence
Create exactly:
`TCRMMT_V157_Evidence.zip`

No production commit/push.
Upload Final Report + ZIP to ChatGPT session exactly `TCRMMMT`.
