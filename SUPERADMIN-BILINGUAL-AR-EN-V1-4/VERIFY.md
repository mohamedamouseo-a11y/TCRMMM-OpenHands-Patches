# Super Admin Bilingual AR/EN V1.4 — Verification

Target: `/var/www/TCRMMT`

## Safety
- Start with `git status --short`.
- Do not reset, clean, restore, commit, or push.
- Apply only `apply_superadmin_bilingual_v1_4.py` once.
- Expected project file changed by this patch: `server/superAdminUiPolish.ts` only.
- Do not change DB, APIs, Auth, Routes, Permissions, Billing/Subscription logic, Business Logic, or Navigation handlers.

## Required baseline
Confirm these markers exist before applying:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_1`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_2`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_3`

## Technical checks
Run in order:
1. `git diff --check`
2. `npm run check`
3. `npm run build`

Only if all pass, restart `tamiyouz-crm` only.

## Final browser gate
Use real Playwright viewport emulation. Verify EN=`lang=en dir=ltr`, AR=`lang=ar dir=rtl`, language persists after Refresh, and page horizontal overflow is 0px at 1440x900, 1024x768, 768x900, and 390x844.

Audit visible text nodes plus `placeholder`, `title`, `aria-label`, and button/input values. Exclude only real record data and technical values: company/user names, emails, IDs, URLs, slugs, tokens, repository/branch/commit values, product names, plan identifiers, and raw technical identifiers.

Required EN surfaces: Login, Overview, Companies, Tenant Details, Users, Platform Admins, Activity, Audit Log, GitHub Sync, Evolution API, Tara APIs, Plans Catalog, Plan Editor, Company Overrides, Commercial/Billing/Subscriptions, Settings/Source Code.

Required AR surfaces: the same surfaces, with ordinary static English UI treated as failure except legitimate technical/product terms.

Recheck specifically all V1.3 failures: Overview KPI labels and search attributes; Companies pagination/helpers/attributes; Users KPI/filter labels; Activity/Audit helpers; GitHub mixed Arabic/English labels; Evolution helper/status text; Plans catalog feature names/descriptions/limits; Commercial labels and Arabic mixed headings.

Navigation structure must still pass:
- `#githubSyncNav` -> `#sec-github`
- `#evolutionApiNav` -> `#sec-evolution-api` at 1440 and 768.

## Evidence
Capture at least:
1. Login EN 1440
2. Login AR 1440
3. Overview EN 1440
4. Overview AR 1440
5. Companies EN 1024
6. Users EN 1024
7. Tenant Details EN 1024
8. Activity EN 1440
9. Audit EN 1440
10. Settings EN 390
11. Settings AR 390
12. GitHub Sync EN 1440
13. Evolution API EN 1440
14. Plans Catalog EN 1440
15. Plans Catalog AR 1440
16. Commercial EN 1440
17. Commercial AR 1440

Final report must contain a section exactly named `UNTRANSLATED STATIC UI`. Acceptance requires exactly `NONE FOUND` after valid technical/data exclusions. If any static UI remains untranslated, do not fix it manually; report text, language, page, selector/attribute, and screenshot, then stop.