# TCRMMT Super Admin Bilingual V1.33 — Companies EN Retry + Audit EN Options Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_33.py` to `/var/www/TCRMMT`.

V1.32 passed apply/build/dist/runtime. Its latest fresh-browser rerun stopped at Companies EN because `button.btn.retryProvisionBtn` remained Arabic as `إعادة التجهيز`. An earlier V1.32 browser pass in the same evidence also proved Audit Log EN `#auditSeverity` retained ordinary static Arabic/mixed options: `كل الأحداث`, `مدفوعات`, `فواتير`, and `Login كأدمن`.

V1.33 closes both evidence-backed regressions in one page-scoped final pass:
- Companies `#tenants`: `إعادة التجهيز` ↔ `Retry provisioning`
- Audit `#audit`: canonical EN/AR event-type options

Do not translate runtime/domain data such as company/person names, emails, dates/timestamps, IDs, paths, product/plan values, role/runtime values, repository/branch/SHA values, URLs/IPs, event payload data, or operational status values such as `فشل التجهيز`.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_32_GITHUB_SYNC_AR_REMAINING_STATIC_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_33.py`

Run it twice.

First run must print:
`Applied Super Admin Bilingual V1.33 Companies EN retry + Audit EN options closure runtime.`

Second run must print:
`Super Admin bilingual V1.33 Companies EN retry + Audit EN options closure already applied; no changes made.`

## Safety
No manual source edits, reset, clean, restore, commit, push, DB/migration changes, Nginx changes, or unrelated PM2 changes.

Only `server/superAdminUiPolish.ts` may be modified.

## Static/build gates
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

## Dist gate
`dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_33_COMPANIES_EN_RETRY_AUDIT_EN_OPTIONS_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V133`
- `/super-admin/bilingual-v133.js`
- `superadmin-bilingual-v133`

## Restart / readiness
Only after all gates pass:
`pm2 restart tamiyouz-crm`

Use readiness polling on port `3002` for up to 90 seconds.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v133.js?v=superadmin-bilingual-v133`

Expected: HTTP 200, JavaScript Content-Type, `Cache-Control: no-store`, and V133 runtime marker.

## Browser QA
Use a fresh browser context and disable cache.

### Regression sequence
Re-run EN + AR:
1. Users
2. Overview
3. Companies
4. Tenant Details
5. Platform Admins
6. Activity
7. Audit Log
8. GitHub Sync

Any genuine ordinary untranslated static UI = STOP immediately.

### Companies EN gate
Open `#tenants`, `lang="en"`, `dir="ltr"`.

For every visible `button.retryProvisionBtn`, require exact:
- `Retry provisioning`

Forbid:
- `إعادة التجهيز`

The operational row status `فشل التجهيز` is excluded from this translation gate as runtime/operational data, per V1.32 evidence classification.

Expected:
`COMPANIES EN RETRY ACTION: PASS`

### Companies AR gate
Open `#tenants`, `lang="ar"`, `dir="rtl"`.

For every visible `button.retryProvisionBtn`, require:
- `إعادة التجهيز`

Forbid:
- `Retry provisioning`

Expected:
`COMPANIES AR RETRY ACTION: PASS`

### Audit Log EN gate
Open `#audit`, `lang="en"`, `dir="ltr"`.

For `select#auditSeverity` require these visible option texts by value:
- `""` → `All events`
- `payment` → `Payments`
- `invoice` → `Invoices`
- `impersonate` → `Admin login`
- `hard_delete` → `Risk`

Forbid:
- `كل الأحداث`
- `مدفوعات`
- `فواتير`
- `Login كأدمن`
- `دخول كأدمن`
- `خطر`

Also preserve all previously-passed Audit Log EN headings/actions.

Expected:
`AUDIT LOG EN STATIC UI: NONE FOUND`

### Audit Log AR gate
Open `#audit`, `lang="ar"`, `dir="rtl"`.

For `select#auditSeverity` require:
- `""` → `كل الأحداث`
- `payment` → `مدفوعات`
- `invoice` → `فواتير`
- `impersonate` → `دخول كأدمن`
- `hard_delete` → `خطر`

Forbid the English counterparts in that select.

Expected:
`AUDIT LOG AR STATIC UI: NONE FOUND`

### GitHub Sync
After all prior regressions pass, re-run full GitHub Sync EN and AR gates from V1.32/V1.31.

Expected:
- `GITHUB SYNC EN STATIC UI: NONE FOUND`
- `GITHUB SYNC AR STATIC UI: NONE FOUND`

## Continue remaining Full Audit
Only if every regression above and GitHub Sync EN/AR PASS, continue EN + AR:
1. Evolution API
2. Tara APIs
3. Plans Catalog
4. Plan Editor
5. Company Overrides
6. Commercial
7. Billing
8. Subscriptions
9. Settings
10. Source Code

On first genuine ordinary untranslated static UI: **STOP immediately. Do not fix manually.**

Record language, page/hash, exact text, untranslated segment, selector/attribute, raw browser finding, and screenshot.

Send `TCRMMT_V133_Evidence.zip` plus final report. No commit or push.
