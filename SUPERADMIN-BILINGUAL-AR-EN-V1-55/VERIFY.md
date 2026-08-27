# TCRMMT Super Admin Bilingual V1.55 — VERIFY

## Purpose
V1.54-R1 browser continuation found one genuine Evolution AR static blocker: `Base URL`. V1.55 extends the existing Evolution canonical pair map with `Base URL` ↔ `الرابط الأساسي` and includes Evolution field labels in the existing v140 selector. No business logic or Evolution values are changed.

## Patch
- target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`
- marker: `SUPER_ADMIN_BILINGUAL_AR_EN_V1_55_EVOLUTION_API_BASE_URL_LABEL_CLOSURE`
- runtime: `SUPER_ADMIN_BILINGUAL_RUNTIME_V155`
- asset: `/super-admin/bilingual-v155.js`
- cache key: `superadmin-bilingual-v155`

## Preconditions
Production stays on `master`. Allowed cumulative tracked modified files only: `server/_core/index.ts`, `server/superAdminUiPolish.ts`. Require `SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_R1_COMPANY_OVERRIDES_BUILD_SYNTAX_REPAIR`. No reset/clean/restore and no manual edits.

## Apply
Run the official script twice. First output must be `Applied Super Admin Bilingual V1.55 Evolution API Base URL label closure.` Second output must be `Super Admin bilingual V1.55 Evolution API Base URL label closure already applied; no changes made.`

## Gates
Run `git diff --check`, `npm run check`, `npm run build`. Confirm source/dist marker, V155 runtime, asset path and cache key. Restart only `tamiyouz-crm` exactly once after all gates pass. New PM2 start epoch must be strictly greater than `dist/index.js` mtime. Port 3002 readiness <=90s.

## Asset
Direct/Public `/super-admin/bilingual-v155.js?v=superadmin-bilingual-v155` three times each: HTTP 200, JavaScript content type, no-store, V155 marker, not HTML.

## Browser primary
Fresh authenticated browser, cache disabled, read-only. Evolution EN direct/hash remains English. Natural AR must show `الرابط الأساسي` for the sibling label of `#evolutionBaseUrl`; exact English `Base URL` is forbidden there. Continue the full audit only after Evolution EN/AR pass.

## Continue audit
Tara EN/AR, Plans Catalog/Editor EN/AR, query precedence, Company Overrides EN/AR, then Commercial EN/AR, Billing EN/AR, Subscriptions EN/AR, Settings EN/AR, Source Code EN/AR. Stop at the first genuine ordinary untranslated static UI. Exclude agreed runtime/domain/catalog values. No production commit/push.

## Evidence
Create `TCRMMT_V155_Evidence.zip` and upload it plus the final report to ChatGPT session exactly `TCRMMMT`.
