# TCRMMT Super Admin Bilingual V1.56 — VERIFY

## Purpose
V1.55 evidence proves `Base URL` field label is closed in Evolution AR and exposes the next genuine static blocker `API Token`; the same captured AR surface also shows `Webhook Signing Secret`, while the status cards contain `Base URL`, `API Token`, and `Webhook Secret`. V1.56 closes the complete Evolution credential/status label cluster in one page-scoped canonical pass.

## Patch
- target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`
- marker: `SUPER_ADMIN_BILINGUAL_AR_EN_V1_56_EVOLUTION_CREDENTIALS_STATUS_LABELS_CLOSURE`
- runtime: `SUPER_ADMIN_BILINGUAL_RUNTIME_V156`
- asset: `/super-admin/bilingual-v156.js`
- cache key: `superadmin-bilingual-v156`
- no business logic or secret/runtime values are changed

## Canonical labels
EN → AR:
- `Base URL` → `الرابط الأساسي`
- `API Token` → `رمز API`
- `Webhook Signing Secret` → `سر توقيع Webhook`
- `Webhook Secret` → `سر Webhook`

The Evolution selector also covers `#evolutionStatusGrid small` so status-card static labels are canonicalized. Secret values, masked suffixes, URLs, timestamps and runtime states remain excluded.

## Preconditions
Production stays on `master`. Allowed cumulative tracked modified files only: `server/_core/index.ts`, `server/superAdminUiPolish.ts`. Require V1.55 marker. No reset/clean/restore/manual edits.

## Apply
Run official V1.56 script twice.
First exact output:
`Applied Super Admin Bilingual V1.56 Evolution credentials/status labels closure.`
Second exact output:
`Super Admin bilingual V1.56 Evolution credentials/status labels closure already applied; no changes made.`

## Gates
`git diff --check`, `npm run check`, `npm run build` all PASS. Confirm source/dist marker, V156 runtime, asset and cache key. Restart only `tamiyouz-crm` exactly once after gates. PM2 start epoch > `dist/index.js` mtime; port 3002 ready <=90s.

## Asset
Direct/Public `/super-admin/bilingual-v156.js?v=superadmin-bilingual-v156` three times each: HTTP 200, JavaScript content type, no-store, V156 marker, not HTML.

## Browser primary
Fresh authenticated browser, cache disabled, read-only.
Evolution EN direct/hash: exact English labels remain `Base URL`, `API Token`, `Webhook Signing Secret`; status cards use `Base URL`, `API Token`, `Webhook Secret`.
Natural AR: exact static labels must be `الرابط الأساسي`, `رمز API`, `سر توقيع Webhook`; status cards `الرابط الأساسي`, `رمز API`, `سر Webhook`.
Do not expose/read secret values. Stop at first next genuine static blocker only after auditing the full Evolution surface.

## Continue audit
After Evolution EN/AR PASS: Tara EN/AR, Plans Catalog/Editor EN/AR, query precedence, Company Overrides EN/AR, Commercial EN/AR, Billing EN/AR, Subscriptions EN/AR, Settings EN/AR, Source Code EN/AR. Keep existing domain/runtime/catalog exclusions. No production commit/push.

## Evidence
Create `TCRMMT_V156_Evidence.zip` and upload Final Report + ZIP to ChatGPT session exactly `TCRMMMT`.
