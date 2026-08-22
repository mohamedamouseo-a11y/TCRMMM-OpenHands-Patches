# Super Admin Bilingual AR/EN V1.6 — VERIFY

## Purpose
V1.6 is a corrective finalization patch for the bilingual Super Admin UI. It repairs the language-control lifecycle (Login, authenticated topbar, floating UI dock), fixes the old language-toggle title semantics, and adds a final canonical post-render sweep for the exact static UI findings confirmed by the V1.5 evidence.

## Safety / Scope
- Target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`
- Presentation/localization only.
- Do not change DB, APIs, Auth logic, Routes, Permissions, Billing/Subscription logic, Business Logic, navigation handlers, or data handlers.
- Do not commit or push from the production worktree.
- Do not use reset/clean/restore.

## Required baseline markers
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_1`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_2`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_3`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_4`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_5`

## Apply
Run once:
`python3 apply_superadmin_bilingual_v1_6.py`

Second run must be a no-op.

## Technical validation
- `git diff --check`
- `npm run check`
- `npm run build`
- Diff names must show only `server/superAdminUiPolish.ts`
- Restart only `tamiyouz-crm` after all checks PASS.

## V1.6-specific functional gate
1. Confirm a visible language button exists on Login.
2. Confirm a visible language button exists in authenticated topbar.
3. Confirm a language button exists in `.sa-ui-dock`.
4. In EN: button shows `AR`, title/aria = `Switch to Arabic`.
5. In AR: button shows `EN`, title/aria = `التبديل إلى الإنجليزية`.
6. Switch EN → AR → EN from visible controls; each switch must change `html.lang`, `html.dir`, and `localStorage['tcrm-super-admin-language']` without reload.
7. Refresh after EN and after AR. Both states must persist correctly.

## Delayed post-render gate
For every tested screen, wait at least 2 seconds after navigation/render before the final scan. Scan visible text plus `placeholder`, `title`, and `aria-label`.

### English
No ordinary Arabic static UI. Exempt only real record/data values and technical identifiers (names, emails, IDs, URLs, slugs, tokens, repo/branch/commit values, product names, plan IDs).

### Arabic
No ordinary English static UI except justified technical identifiers/product terms.

## Mandatory V1.5 regression checks
### Arabic Overview
Must not show: `PLATFORM OVERVIEW`, `QUICK COMMANDS`, `ATTENTION`, `USAGE`, `GLOBAL SEARCH`, `SECURITY`, `Owner Only`, `Slug`, `Email`, `حفظ Admin وصلاحيات الشركات`, `إنشاء Workspace جديد`.

### Arabic Login
Must show Arabic brand copy and a visible language button.

### Arabic Plans
Must not show: `Back to Command Center`, `Refresh Data`, `View details`.

### Arabic Commercial
Must not show untranslated `Kill Switch`, `Canary %`, `Grace Days`, `Feature Overrides JSON`, `Limit Overrides JSON`, or the English controlled-enforcement heading.

### English
Recheck the V1.5 leftovers: Overview KPI labels/search attrs, Users subtitle, Activity subtitle, Audit mixed subtitle, GitHub branch/status copy, Evolution subtitle, Commercial security button.

## Navigation
- `#githubSyncNav` => `#sec-github`
- `#evolutionApiNav` => `#sec-evolution-api`
- Evolution at 1440x900 and 768x900.

## Responsive
EN + AR at 1440x900, 1024x768, 768x900, 390x844.
- EN = `lang=en`, `dir=ltr`
- AR = `lang=ar`, `dir=rtl`
- page horizontal overflow = 0
- no clipping / overlap

## Evidence
Provide report + screenshots for Login EN/AR, Overview EN/AR, Companies EN, Users EN, Tenant Details EN, Activity EN, Audit EN, Settings EN/AR, GitHub EN, Evolution EN, Plans EN/AR, Commercial EN/AR.

Report must contain `UNTRANSLATED STATIC UI` and the only acceptance value is `NONE FOUND`.
If anything remains, do not fix it manually; record exact text, language, page, selector/attribute, screenshot and stop.
