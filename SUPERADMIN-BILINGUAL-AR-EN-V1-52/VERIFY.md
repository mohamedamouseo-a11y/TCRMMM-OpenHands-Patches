# TCRMMT Super Admin Bilingual V1.52 — VERIFY

## Purpose

V1.51 evidence proves the Plans language handoff itself is fixed:

- normal Main → Plans navigation reaches `/super-admin/plans?lang=en`
- final Plans language state is `lang=en`, `dir=ltr`, `data-sa-lang=en`
- stored language is `en`
- `#status` is the required English runtime status

The first genuine remaining ordinary static blocker is:

`Companies Management والباقات على مستوى المنصة.`

This is a mixed-language phrase created when an earlier generic bilingual sweep translates the Arabic prefix `إدارة الشركات` before the Plans page-scoped finalizer sees the entire sentence.

V1.52 adds a narrowly page-scoped canonical closure for the observed mixed form and its canonical AR/EN counterparts. It does not modify plan data, APIs, persistence, or business logic.

## Official patch

Repository:
`mohamedamouseo-a11y/TCRMMM-OpenHands-Patches`

Branch:
`superadmin-bilingual-ar-en-v1-52`

Folder:
`SUPERADMIN-BILINGUAL-AR-EN-V1-52`

Files:
- `apply_superadmin_bilingual_v1_52.py`
- `VERIFY.md`

Target:
`/var/www/TCRMMT`

Production branch stays `master`.

## Allowed cumulative tracked modified scope

Only:
- `server/superAdminUiPolish.ts`
- `server/_core/index.ts`

V1.52 itself modifies only:
- `server/superAdminUiPolish.ts`

Any other tracked modified file: STOP.

No reset/clean/restore.

## Preflight

```bash
cd /var/www/TCRMMT
git status --short
git branch --show-current
git rev-parse HEAD
```

Must remain `master`.

Confirm V1.51 marker exists:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1_51_PLANS_LANGUAGE_NAV_PERSISTENCE`

Confirm V1.52 marker is absent before first apply:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1_52_PLANS_MIXED_COMPANIES_PLATFORM_CLOSURE`

## Apply twice

Run official V1.52 script twice.

First expected exactly:

`Applied Super Admin Bilingual V1.52 Plans mixed companies/platform closure.`

Second expected exactly:

`Super Admin bilingual V1.52 Plans mixed companies/platform closure already applied; no changes made.`

No manual edits.

## Static gates

Run:

```bash
git diff --check
npm run check
npm run build
```

All PASS.

Confirm source/dist:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_52_PLANS_MIXED_COMPANIES_PLATFORM_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V152`
- `/super-admin/bilingual-v152.js`
- `superadmin-bilingual-v152`

## Restart

Restart only:

```bash
pm2 restart tamiyouz-crm
```

Exactly one restart in this V1.52 cycle.

Capture `dist/index.js` mtime first. New PM2 start epoch must be strictly greater than dist mtime. If stale: STOP.

Port 3002 readiness <=90 sec.

## Runtime asset

Direct 3x:

`http://127.0.0.1:3002/super-admin/bilingual-v152.js?v=superadmin-bilingual-v152`

Public 3x:

`https://tcrmmm.tamiyouz.com/super-admin/bilingual-v152.js?v=superadmin-bilingual-v152`

Every attempt:
- HTTP 200
- JavaScript content type
- Cache-Control no-store
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V152`
- no HTML fallback

## Regression — Evolution

Fresh authenticated browser, cache disabled, read-only.

Re-run V1.46 direct Evolution + hash away/back and EN/AR canonical audit.

Expected:
- `EVOLUTION API EN STATIC UI: NONE FOUND`
- `EVOLUTION API AR STATIC UI: NONE FOUND`

No mutation.

## Regression — Tara

Repeat:
AR main → Tara AR → back → natural EN → Tara EN without forced refresh.

Expected:
- `TARA APIs EN STATIC UI: NONE FOUND`
- `TARA APIs AR STATIC UI: NONE FOUND`

Modal open/close only. No Save/Test/Disable/Delete.

## Plans language handoff regression

Using the normal visible Main language control:

### EN
Before Plans:
- `lang=en`
- `dir=ltr`
- `data-sa-lang=en`
- stored language `en`

Click normal Plans nav.

Final URL must contain:
`/super-admin/plans?lang=en`

Final Plans:
- `lang=en`
- `dir=ltr`
- `data-sa-lang=en`
- stored language `en`

### AR
Repeat naturally from Main in AR.

Final URL must contain:
`/super-admin/plans?lang=ar`

Final state AR/RTL.

## PRIMARY — Plans Catalog EN blocker closure

Open Plans through the normal EN handoff.

The following exact V1.51 blocker is forbidden:

`Companies Management والباقات على مستوى المنصة.`

Also forbidden:
- `Companies Management والباقات على مستوى المنصة`
- `إدارة الشركات والباقات على مستوى المنصة.`
- `إدارة الشركات والباقات على مستوى المنصة`

If this sentence is present in the visible Plans Catalog surface, EN canonical must be:

`Manage companies and plans across the platform.`

Then continue the full Plans Catalog EN static audit from the beginning.

Expected:

`PLANS CATALOG EN STATIC UI: NONE FOUND`

## Plan Editor EN

Select one existing plan read-only.

Do not:
- Clone to draft
- Save draft
- Publish version
- persist any field

Expected:

`PLAN EDITOR EN STATIC UI: NONE FOUND`

## Plans Catalog + Plan Editor AR

Use normal AR handoff.

If the V1.52 sentence is visible, canonical AR must be:

`إدارة الشركات والباقات على مستوى المنصة.`

Expected:
- `PLANS CATALOG AR STATIC UI: NONE FOUND`
- `PLAN EDITOR AR STATIC UI: NONE FOUND`

## Query precedence regression

Repeat V1.51 read-only query precedence proof:
- stored AR + `?lang=en` → EN/LTR
- stored EN + `?lang=ar` → AR/RTL

## Continue Full Audit

Only after Evolution, Tara, Plans Catalog EN/AR, Plan Editor EN/AR all pass.

Continue:
1. Company Overrides EN/AR
2. Commercial EN/AR
3. Billing EN/AR
4. Subscriptions EN/AR
5. Settings EN/AR
6. Source Code EN/AR

At first genuine ordinary untranslated static UI:
STOP immediately and capture exact evidence.

Do not manually fix.
Do not reset/clean/restore.
Do not commit/push production.

Exclude domain/runtime data:
names, emails, IDs, dates/timestamps, URLs/IPs, roles, plan/product/provider values, slugs, versions, counts, repo/branch/SHA, masked secrets, raw technical errors.

## Evidence

Create:

`TCRMMT_V152_Evidence.zip`

Include:
- preflight/apply/no-op
- static gates
- restart/stale guard/readiness
- Direct/Public asset 3x
- Evolution/Tara regressions
- Plans EN/AR language handoff
- exact V1.51 blocker closure proof
- Plans Catalog/Editor EN/AR audits
- next Full Audit blocker if any
- screenshots

No production commit/push.

Upload Final Report + `TCRMMT_V152_Evidence.zip` to ChatGPT session exactly:

`TCRMMMT`
