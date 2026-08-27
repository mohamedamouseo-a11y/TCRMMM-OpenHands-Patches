# TCRMMT Super Admin Bilingual V1.54-R1 — Build Syntax Repair

## Purpose

V1.54 applied successfully and its second apply was an exact no-op, but `npm run build` stopped before restart/runtime QA.

Confirmed build blocker: two JavaScript backtick template literals were inserted inside the larger TypeScript template literal that emits the bilingual browser runtime in `server/superAdminUiPolish.ts`. esbuild therefore treated the inner backtick as the end of the outer TypeScript template and failed with `Expected ";" but found "المستخدم"`.

V1.54-R1 changes only those two emitted-runtime string constructions from nested backtick templates to ordinary single-quoted string concatenation.

It does not alter V1.54 translation mappings, Company Overrides behavior, runtime version V154, asset path/cache key, business logic, data, or APIs.

## Patch identity

Repository: `mohamedamouseo-a11y/TCRMMM-OpenHands-Patches`

Branch: `superadmin-bilingual-ar-en-v1-54-r1`

Folder: `SUPERADMIN-BILINGUAL-AR-EN-V1-54-R1`

Files:
- `apply_superadmin_bilingual_v1_54_r1.py`
- `VERIFY.md`

Target: `/var/www/TCRMMT`

Production branch remains `master`.

## Current production expectation

V1.54 is already present in source from the prior attempt. The prior task did NOT restart PM2 after the failed build.

Allowed cumulative tracked modified files remain only:
- `server/_core/index.ts`
- `server/superAdminUiPolish.ts`

Any third tracked modified file: STOP.

No reset/clean/restore.

## Preflight

Capture:

```bash
cd /var/www/TCRMMT
git status --short
git branch --show-current
git rev-parse HEAD
```

Confirm:
- branch `master`
- V1.54 marker exists: `SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_COMPANY_OVERRIDES_FULL_STATIC_DYNAMIC_CLOSURE`
- V1.54-R1 marker is absent before first repair
- source still contains exactly the two broken nested-template `waHint` forms identified by the failed V1.54 build

Do not re-run the original V1.54 apply script.

## Apply V1.54-R1 twice

Run official R1 script twice.

First expected exactly:

`Applied Super Admin Bilingual V1.54-R1 Company Overrides build syntax repair.`

Second expected exactly:

`Super Admin bilingual V1.54-R1 Company Overrides build syntax repair already applied; no changes made.`

No manual edit.

## Repair proof

After apply:
- V1.54 marker remains present
- V1.54-R1 marker is present
- neither broken nested-backtick `waHint` form remains
- both repaired `waHint` branches use string concatenation
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V154` remains unchanged
- `/super-admin/bilingual-v154.js` remains unchanged
- `superadmin-bilingual-v154` remains unchanged

## Static gates

Run:

```bash
git diff --check
npm run check
npm run build
```

All must PASS.

If build fails again: STOP. No restart. No manual fix.

If build passes, confirm source + dist contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_COMPANY_OVERRIDES_FULL_STATIC_DYNAMIC_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_R1_COMPANY_OVERRIDES_BUILD_SYNTAX_REPAIR`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V154`
- `/super-admin/bilingual-v154.js`
- `superadmin-bilingual-v154`

## Restart

Only after all static gates PASS.

Capture `dist/index.js` mtime.

Execute exactly once:

```bash
pm2 restart tamiyouz-crm
```

Do not queue or paste a duplicate restart.

New PM2 process start epoch must be strictly greater than `dist/index.js` mtime.

Port 3002 readiness <= 90 seconds.

## Runtime asset

Direct 3x:

`http://127.0.0.1:3002/super-admin/bilingual-v154.js?v=superadmin-bilingual-v154`

Public 3x:

`https://tcrmmm.tamiyouz.com/super-admin/bilingual-v154.js?v=superadmin-bilingual-v154`

Every attempt:
- HTTP 200
- JavaScript content type
- Cache-Control no-store
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V154`
- not HTML fallback

## Regression

Fresh authenticated Super Admin browser, cache disabled, read-only.

Verify:
- Evolution EN/AR + direct/hash
- Tara AR then natural EN, modal open/close only
- Plans Catalog EN/AR
- Plan Editor EN/AR
- V1.53 limits helper in both languages
- query precedence

Continue excluding runtime/domain/catalog values exactly as previously defined.

## PRIMARY — Company Overrides EN

Natural Main EN → Plans → Companies & Overrides.

Confirm `lang=en`, `dir=ltr`, `data-sa-lang=en`.

The old blocker is forbidden:

`تعيين الباقات وضبط الحدود والاستثناءات وReview النتيجة الفعلية لكل شركة.`

Canonical intro:
- `Companies Management`
- `Companies & Overrides`
- `Assign plans, configure limits and overrides, and review the effective result for each company.`
- `Per-company control`

Audit the full Company Overrides static surface. You may select one existing company read-only to expose the editor.

Do NOT:
- Assign Plan
- Save Mode
- Save Overrides
- Save Assistant Identity
- persist fields

Exclude names, emails, ids, slugs, plan/domain/catalog values, counts and runtime values.

Expected: `COMPANY OVERRIDES EN STATIC UI: NONE FOUND`

## Company Overrides AR

Natural AR handoff.

Canonical intro:
- `إدارة الشركات`
- `الشركات والاستثناءات`
- `تعيين الباقات وضبط الحدود والاستثناءات ومراجعة النتيجة الفعلية لكل شركة.`
- `تحكم لكل شركة`

Same read-only audit and exclusions.

Expected: `COMPANY OVERRIDES AR STATIC UI: NONE FOUND`

## Continue Full Audit

Only after Company Overrides EN/AR PASS:

1. Commercial EN
2. Commercial AR
3. Billing EN
4. Billing AR
5. Subscriptions EN
6. Subscriptions AR
7. Settings EN
8. Settings AR
9. Source Code EN
10. Source Code AR

At first genuine untranslated ordinary static UI: STOP immediately, capture exact evidence, and do not fix.

No production commit/push.

## Evidence

Create exactly: `TCRMMT_V154_R1_Evidence.zip`

Include:
- prior blocker confirmation
- R1 apply + exact no-op
- repaired-source proof
- all static gates
- single restart/stale guard/readiness if build passes
- Direct/Public asset 3x
- regressions
- Company Overrides EN/AR
- continued Full Audit and first blocker if any

Upload Final Report + ZIP to ChatGPT session exactly: `TCRMMMT`

No production commit. No push.
