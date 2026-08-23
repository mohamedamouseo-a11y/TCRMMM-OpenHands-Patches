# TCRMMT Super Admin Bilingual V1.19 — Companies AR Plan Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_19.py` to `/var/www/TCRMMT`.

This patch closes the first genuine ordinary untranslated static UI finding from V1.18 Browser QA on Companies / Tenants Arabic:

- `الحالة، Plan، الصحة والإجراءات.` → `الحالة، الخطة، الصحة والإجراءات.`

The patch adds the bilingual static label pair `Plan` ↔ `الخطة` to the localization chain. Do not translate plan/product values such as `Enterprise`, `enterprise`, or `starter`, nor company/user names, paths, emails, dates, IDs, or runtime data.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_18_USERS_MIXED_HEADER_CLOSURE`

## Apply
Run twice. First run must print:

`Applied Super Admin Bilingual V1.19 Companies AR Plan closure runtime.`

Second run must be a no-op.

## Static gates
Only `server/superAdminUiPolish.ts` may change.

Run:
- `git diff --check`
- `npm run check`
- `npm run build`

Dist must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_19_COMPANIES_AR_PLAN_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V119`
- `/super-admin/bilingual-v119.js`
- `superadmin-bilingual-v119`

## Restart / readiness
Only after all static/build/dist gates PASS:
- restart `tamiyouz-crm` only.
- poll port `3002` for up to 90 seconds; do not use a fixed short sleep as a failure gate.

Verify Direct + Public:
- `/super-admin` = HTTP 200
- `/super-admin/bilingual-v119.js?v=superadmin-bilingual-v119` = HTTP 200
- JavaScript content type
- `Cache-Control: no-store`
- runtime marker `SUPER_ADMIN_BILINGUAL_RUNTIME_V119`

## Browser QA
Use a fresh browser context with cache disabled.

First re-check regression gates already passed under V1.18:
- Users EN / AR
- Overview EN / AR
- Companies EN

### Companies AR — blocking gate
Open Companies / Tenants in Arabic and verify:
- `lang="ar"`
- `dir="rtl"`
- subtitle contains exactly: `الحالة، الخطة، الصحة والإجراءات.`
- ordinary untranslated `Plan` is absent from that subtitle.
- `نسخ المسار`, `تفاصيل`, `تجديد`, `دخول` remain correct.
- pagination remains Arabic.
- plan/product values such as `Enterprise`, `enterprise`, `starter` remain runtime/domain data and are not treated as translation failures.

Capture the subtitle node text + selector and one screenshot.

### Continue the interrupted audit
If Companies AR passes, continue:
- Tenant Details EN / AR
- Platform Admins EN / AR
- Activity EN / AR
- Audit Log EN / AR
- GitHub Sync EN / AR
- Evolution API EN / AR
- Tara APIs EN / AR
- Plans Catalog EN / AR
- Plan Editor EN / AR
- Company Overrides EN / AR
- Commercial EN / AR
- Billing EN / AR
- Subscriptions EN / AR
- Settings EN / AR
- Source Code EN / AR

Stop immediately on the first genuine ordinary untranslated static UI finding. Do not fix it manually. Record:
- language
- page
- exact text
- selector / attribute
- raw browser finding
- screenshot

## Final report
Include:

```text
RUNTIME V119: PASS/FAIL
USERS EN: PASS/FAIL
USERS AR: PASS/FAIL
OVERVIEW EN: PASS/FAIL
OVERVIEW AR: PASS/FAIL
COMPANIES EN: PASS/FAIL
COMPANIES AR: PASS/FAIL
TENANT DETAILS EN: PASS/FAIL/NOT RUN
TENANT DETAILS AR: PASS/FAIL/NOT RUN
NEXT TRANSLATION BLOCKER:
UNTRANSLATED STATIC UI: NONE FOUND / FOUND
```

If the complete remaining audit reaches the end with no blocker, final acceptance is only:

`UNTRANSLATED STATIC UI: NONE FOUND`

## Safety
No reset / clean / restore / manual source edits / commit / push. No Nginx, DB, migrations, startup-mode changes, or unrelated PM2 diagnostics.
