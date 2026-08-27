# TCRMMT Super Admin Bilingual V1.54 — VERIFY

## Purpose
Close the first genuine Full Audit blocker in Companies & Overrides EN:

`تعيين الباقات وضبط الحدود والاستثناءات وReview النتيجة الفعلية لكل شركة.`

V1.54 is a page-scoped full ordinary-UI closure for `#tenantsView` on `/super-admin/plans`. It canonicalizes Company Overrides EN/AR static copy, observed mixed aliases, placeholders, safe dynamic helper/status copy, and snapshot labels while intentionally leaving tenant/company names, plan/domain values, ids, slugs, counts, feature/limit catalog data, and runtime values untouched.

## Patch
Repository: `mohamedamouseo-a11y/TCRMMM-OpenHands-Patches`
Branch: `superadmin-bilingual-ar-en-v1-54`
Folder: `SUPERADMIN-BILINGUAL-AR-EN-V1-54`

Files:
- `apply_superadmin_bilingual_v1_54.py`
- `VERIFY.md`

Base: V1.53 head `fe74b25d06591de52c99415dccdb73115c3f00ae`

Target: `/var/www/TCRMMT`
Production branch remains `master`.

## Apply
Run official script twice.

Expected first:
`Applied Super Admin Bilingual V1.54 Company Overrides full static/dynamic closure.`

Expected second:
`Super Admin bilingual V1.54 Company Overrides full static/dynamic closure already applied; no changes made.`

No manual edits.

## Allowed cumulative tracked scope
Only:
- `server/superAdminUiPolish.ts`
- `server/_core/index.ts`

V1.54 itself modifies only `server/superAdminUiPolish.ts`.

Any third tracked file: STOP.
No reset/clean/restore.

## Gates
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All PASS.

Confirm source/dist markers:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_COMPANY_OVERRIDES_FULL_STATIC_DYNAMIC_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V154`
- `/super-admin/bilingual-v154.js`
- `superadmin-bilingual-v154`

## Restart
Restart only `tamiyouz-crm`, exactly once.
New PM2 start epoch must be strictly greater than `dist/index.js` mtime.
Port 3002 readiness <= 90 sec.

## Runtime asset
Direct 3x and Public 3x for:
`/super-admin/bilingual-v154.js?v=superadmin-bilingual-v154`

Every attempt:
- HTTP 200
- JavaScript Content-Type
- Cache-Control no-store
- V154 marker present
- not HTML fallback

## Regression
Fresh authenticated browser, cache disabled, read-only.

Re-run:
- Evolution EN/AR + direct/hash
- Tara AR -> Main -> EN -> Tara EN, modal open/close only
- Plans Catalog EN/AR
- Plan Editor EN/AR
- Query precedence

Do not mutate Plans/Tara data.

## PRIMARY — Company Overrides EN
Open Main EN -> Plans naturally -> Companies & Overrides.

Final:
- `/super-admin/plans?lang=en`
- `lang=en`
- `dir=ltr`
- `data-sa-lang=en`

The old blocker is forbidden:
`تعيين الباقات وضبط الحدود والاستثناءات وReview النتيجة الفعلية لكل شركة.`

Canonical intro must be:
- `Companies Management`
- `Companies & Overrides`
- `Assign plans, configure limits and overrides, and review the effective result for each company.`
- `Per-company control`

Audit the entire Company Overrides static surface, including hidden/read-only editor UI without saving.

Expected:
`COMPANY OVERRIDES EN STATIC UI: NONE FOUND`

Exclude company names, emails, ids, plan names/slugs/versions/counts, feature/limit catalog data, runtime values.

## Company Overrides AR
Natural AR handoff, open Companies & Overrides.

Expected canonical intro:
- `إدارة الشركات`
- `الشركات والاستثناءات`
- `تعيين الباقات وضبط الحدود والاستثناءات ومراجعة النتيجة الفعلية لكل شركة.`
- `تحكم لكل شركة`

Expected:
`COMPANY OVERRIDES AR STATIC UI: NONE FOUND`

No Save/Assign/Override/Identity mutation.

## Continue Full Audit
Only after Company Overrides EN/AR PASS:
1. Commercial EN/AR
2. Billing EN/AR
3. Subscriptions EN/AR
4. Settings EN/AR
5. Source Code EN/AR

STOP at first genuine ordinary untranslated static UI.
Capture exact language/route/tab/text/selector/screenshot.
Do not fix manually.

## Evidence
Create exactly:
`TCRMMT_V154_Evidence.zip`

Upload Final Report + ZIP into ChatGPT session exactly:
`TCRMMMT`

No production commit/push.
