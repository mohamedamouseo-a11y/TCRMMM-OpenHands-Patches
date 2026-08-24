# TCRMMT Super Admin Bilingual V1.21 — Platform Admins AR Full Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_21.py` to `/var/www/TCRMMT`.

V1.20 passed runtime/build and all regression gates through Tenant Details EN/AR. The V1.20 raw Platform Admins AR scan proved two genuine ordinary static blockers:
- `PLATFORM ADMINISTRATION`
- `+ إضافة Admin`

V1.21 closes both together so Platform Admins AR can be audited as a complete page instead of one finding per patch.

Do not translate user/company names, emails, dates, IDs, paths, tenant/product/plan values, or runtime/domain data. Existing row role values such as `Super Admin` are treated as role/runtime values for this audit unless a later explicit gate classifies them otherwise.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_20_PLATFORM_ADMINS_AR_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_21.py`

Run it twice.
First run must print:
`Applied Super Admin Bilingual V1.21 Platform Admins AR full closure runtime.`

Second run must be no-op:
`Super Admin bilingual V1.21 Platform Admins AR full closure already applied; no changes made.`

## Safety
No:
- manual source edits
- reset / clean / restore
- commit / push
- DB or migration changes
- Nginx changes
- unrelated PM2 changes

## Static gates
Only:
`server/superAdminUiPolish.ts`

may change.

Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

## Dist gate
Before restart, `dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_21_PLATFORM_ADMINS_AR_FULL_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V121`
- `/super-admin/bilingual-v121.js`
- `superadmin-bilingual-v121`

If any marker is missing: STOP.

## Restart / readiness
Only after all static/build/dist gates pass:

`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds. Do not fail on a fixed short sleep.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v121.js?v=superadmin-bilingual-v121`

Expected:
- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V121`

## Regression gates
Fresh browser context, cache disabled.

Re-run:
- Users EN / AR
- Overview EN / AR
- Companies EN / AR
- Tenant Details EN / AR

Any regression = STOP.

## Platform Admins AR full gate
Open:
`#platform-admins`

Set Arabic and verify:
- `lang="ar"`
- `dir="rtl"`

The V1.20 subtitle must remain canonical:
`إدارة حسابات مسؤولي المنصة وتوزيع الشركات`

The eyebrow must be Arabic:
`إدارة المنصة`

The create action must be Arabic:
`+ إضافة مسؤول`

Explicitly forbid:
- `PLATFORM ADMINISTRATION`
- `+ إضافة Admin`
- `+ Add Admin`
- `+ Add مسؤول`

Scan:
- visible text
- placeholders
- title
- aria-label

Expected:
`PLATFORM ADMINS AR STATIC UI: NONE FOUND`

Names, emails, dates, IDs, paths, tenant/product/plan values, and runtime/domain data are excluded.

## Platform Admins EN gate
Switch to English and verify:
- `lang="en"`
- `dir="ltr"`

Expected canonical values:
- `PLATFORM ADMINISTRATION`
- `Manage Platform Admin accounts and company assignments`
- `+ Add Admin`

No ordinary Arabic static leakage.

Expected:
`PLATFORM ADMINS EN STATIC UI: NONE FOUND`

## Continue remaining Full Audit
Only if Platform Admins EN and AR both PASS, continue EN + AR:

1. Activity
2. Audit Log
3. GitHub Sync
4. Evolution API
5. Tara APIs
6. Plans Catalog
7. Plan Editor
8. Company Overrides
9. Commercial
10. Billing
11. Subscriptions
12. Settings
13. Source Code

On the first genuine ordinary untranslated static UI:
**STOP immediately. Do not fix manually.**

Record:
- language
- page/hash
- exact text
- untranslated segment
- selector / attribute
- raw browser finding
- screenshot

## Final report
Include:
```text
RUNTIME V121:
USERS EN:
USERS AR:
OVERVIEW EN:
OVERVIEW AR:
COMPANIES EN:
COMPANIES AR:
TENANT DETAILS EN:
TENANT DETAILS AR:
PLATFORM ADMINS EN:
PLATFORM ADMINS AR:
NEXT TRANSLATION BLOCKER:
UNTRANSLATED STATIC UI:
```

Send ZIP Evidence and stop.

No commit or push.
