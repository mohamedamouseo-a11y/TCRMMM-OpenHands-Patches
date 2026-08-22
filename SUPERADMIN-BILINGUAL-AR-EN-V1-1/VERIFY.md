# VERIFY — Super Admin Bilingual Arabic / English V1.1

Target: `/var/www/TCRMMT`

Patch: `apply_superadmin_bilingual_v1_1.py`

Scope: translation coverage corrective only. Do not change DB, APIs, Auth, Routes, Permissions, Billing/Subscription Logic, Business Logic, or existing handlers.

## Preflight

1. `cd /var/www/TCRMMT`
2. `git status --short`
3. Do not run reset/clean/restore.
4. Confirm V1 is already present:
   - `grep -n "SUPER_ADMIN_BILINGUAL_AR_EN_V1" server/superAdminUiPolish.ts`
5. Apply exactly once:
   - `python3 /tmp/<patch-dir>/apply_superadmin_bilingual_v1_1.py`
6. Confirm marker exactly once:
   - `grep -c "SUPER_ADMIN_BILINGUAL_AR_EN_V1_1" server/superAdminUiPolish.ts`

## Static checks

Run:

- `git diff --check`
- `npm run check`
- `npm run build`

If all pass, restart **only** `tamiyouz-crm`.

## Language behavior

Verify both states:

- English: `lang=en`, `dir=ltr`
- Arabic: `lang=ar`, `dir=rtl`

Verify language switch works without reload and persists after refresh through `tcrm-super-admin-language`.

## Translation coverage audit

Re-run the same live audit that found the V1 gaps. Inspect visible static UI text on:

- Login / Forgot / Reset Password
- Overview
- Companies
- Users
- Platform Admins
- Plans Catalog
- Plan Editor
- Company Overrides
- Commercial / Billing / Subscriptions
- Activity
- Audit Log
- GitHub Sync
- Evolution API
- Tara APIs
- Settings Drawer
- Account / Appearance / Source Code
- Tenant Details

### English mode acceptance

No Arabic static UI should remain. In particular confirm these V1 findings are now English:

- Sidebar/nav: مركز القيادة, الباقات والحدود, الإجراءات والتحليلات, أثر الأنشطة, خروج
- Overview headings: نظرة تنفيذية على المنصة, القرارات السريعة, يحتاج متابعة, تحليلات الاستخدام
- Companies filters/table/actions
- Users / Platform Admins labels
- Activity / Audit Log headings and actions
- Plans Catalog labels
- GitHub Sync / Evolution / Tara static labels
- Settings appearance labels `داكن` / `فاتح`
- Settings Source Code heading/description/loading text

### Arabic mode acceptance

Translate ordinary static UI headings, including:

- Organizations / ORGANIZATIONS
- Users & Access / USERS & ACCESS
- Plans & Commercial / PLANS & COMMERCIAL
- Platform Administration / PLATFORM ADMINISTRATION
- PLATFORM OVERVIEW
- QUICK COMMANDS
- GLOBAL SEARCH
- USAGE
- SECURITY
- ENTERPRISE
- Base URL
- Webhook Signing Secret
- Login brand copy `Platform administration, simplified.`
- Login brand sentence `Secure, multi-tenant control for your entire TCRMMT ecosystem.`

Technical/data values may remain Latin, including TCRMMT, GitHub, API product names, emails, IDs, slugs, URLs, role/data values, commits, tokens, and user/company names.

## Navigation verification

The V1 QA had inconsistent English navigation at 1440 for GitHub Sync / Evolution API. Do **not** modify application logic in this patch.

Re-test using stable element identity (`id`, `data-section`, handler target, or active section id), not translated visible text alone.

At `1440x900` English verify separately:

- Click GitHub Sync nav item -> actual GitHub Sync section becomes visible/active.
- Click Evolution API nav item -> actual Evolution API section becomes visible/active.

Also spot-check at `768x900` English Evolution API.

If a real navigation defect remains after stable selector verification, report exact clicked element, handler/target, active section before/after, and screenshot. Do not fix logic in this task.

## Responsive

Test English + Arabic at:

- 1440x900
- 1024x768
- 768x900
- 390x844

For each record:

- `window.innerWidth`
- `document.documentElement.clientWidth`
- `document.documentElement.scrollWidth`
- page overflow

Acceptance: zero page-level horizontal overflow, no clipping, no overlap, RTL/LTR correct.

## Required screenshots

At minimum:

1. Login English 1440
2. Login Arabic 1440
3. Overview English 1440
4. Overview Arabic 1440
5. Companies English 1024
6. Companies Arabic 1024
7. Settings English 390
8. Settings Arabic 390
9. GitHub Sync English 1440
10. Evolution API English 1440

## Final report

Include sections:

- Static checks
- Language persistence
- Responsive matrix
- Navigation verification
- `UNTRANSLATED STATIC UI`

The final translation gate is PASS only if `UNTRANSLATED STATIC UI` is `NONE FOUND` after excluding legitimate technical/data values.

**Do not commit or push.**
