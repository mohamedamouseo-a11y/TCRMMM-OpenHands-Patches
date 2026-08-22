# Super Admin Bilingual AR/EN V1.3 — Apply & Verify

Target project: `/var/www/TCRMMT`

Patch file: `apply_superadmin_bilingual_v1_3.py`

This is a localization/presentation-only corrective pass derived from the live V1.2 evidence. It must not modify DB, APIs, auth, routes, permissions, billing/subscription logic, business logic, or navigation handlers.

## Apply

1. Record `git status --short`.
2. Do not use `reset`, `clean`, or `restore`.
3. Confirm these markers already exist in `server/superAdminUiPolish.ts`:
   - `SUPER_ADMIN_BILINGUAL_AR_EN_V1`
   - `SUPER_ADMIN_BILINGUAL_AR_EN_V1_1`
   - `SUPER_ADMIN_BILINGUAL_AR_EN_V1_2`
4. Run once:
   - `python3 apply_superadmin_bilingual_v1_3.py`
5. Confirm marker:
   - `SUPER_ADMIN_BILINGUAL_AR_EN_V1_3`

## Technical checks

Run:

- `git diff --check`
- `npm run check`
- `npm run build`

Only if all pass, restart `tamiyouz-crm` and no other process.

## Language behavior

Verify:

- English: `lang=en`, `dir=ltr`
- Arabic: `lang=ar`, `dir=rtl`
- storage key: `tcrm-super-admin-language`
- AR persists after refresh
- EN persists after refresh
- no horizontal page overflow

## Full translation gate

Audit all visible **static UI** in both languages across:

- Login / forgot / reset
- Overview
- Companies
- Create Company drawer
- Subscription drawer
- Tenant Details drawer
- Users
- Platform Admins + Admin drawer
- Activity
- Audit Log
- GitHub Sync
- Evolution API
- Tara APIs
- Plans Catalog
- Plan Editor
- Company Overrides
- Commercial / Billing / Subscriptions
- Settings / Source Code

Exclude only real record/data/technical values such as company/user names, emails, IDs, URLs, slugs, tokens, repository names, branch names, commit SHAs, plan identifiers, and product names such as TCRMMT/GitHub/Evolution API.

### English scan

When English is selected, scan visible text nodes and attributes for Arabic characters. Every Arabic hit must be classified. A hit is acceptable only if it is real user/data content or a technical value. Ordinary UI copy is a FAIL.

Specifically verify the V1.2 failures are gone:

- Overview helper/KPI/quick-command/search/status Arabic copy
- Companies and drawer Arabic labels
- Settings source metadata Arabic labels/status
- GitHub Sync Arabic status/helper labels
- Evolution API Arabic helper/status text
- Plans Catalog/editor Arabic labels and subtitles
- Commercial/Billing Arabic KPI/support text

### Arabic scan

When Arabic is selected, verify ordinary static UI is Arabic and no English UI copy remains, except product/technical terms and real data values.

## Structural navigation

From Overview, verify with IDs and actual active sections:

- click `#githubSyncNav` => `#sec-github` visible and active
- click `#evolutionApiNav` => `#sec-evolution-api` visible and active

Test Evolution at 1440 and 768 widths.

## Responsive matrix

Test both EN and AR:

- 1440×900
- 1024×768
- 768×900
- 390×844

Record:

- `innerWidth`
- `innerHeight`
- `clientWidth`
- `scrollWidth`
- `scrollWidth - clientWidth`
- language
- direction

Acceptance: page horizontal overflow = 0px, no clipping, no overlap.

## Required screenshots

1. Login EN 1440×900
2. Login AR 1440×900
3. Overview EN 1440×900
4. Overview AR 1440×900
5. Companies EN 1024×768
6. Tenant Details EN 1024×768
7. Settings EN 390×844
8. Settings AR 390×844
9. GitHub Sync EN 1440×900
10. Evolution API EN 1440×900
11. Plans Catalog EN 1440×900
12. Commercial EN 1440×900

## Final report gate

The final report must contain a section exactly named:

`UNTRANSLATED STATIC UI`

Final acceptance is allowed only if the value is:

`NONE FOUND`

If any untranslated static UI remains, do not fix it manually. Report exact text, language, page, selector/region, and screenshot evidence, then stop.

Do not commit or push.
