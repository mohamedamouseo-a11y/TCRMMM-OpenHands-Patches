# TCRMMT Super Admin Bilingual V1.22 — Platform Admins EN Count Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_22.py` to `/var/www/TCRMMT`.

V1.21 passed runtime/build and all regressions through Tenant Details EN/AR plus the complete Platform Admins AR gate. The first remaining blocker was in Platform Admins EN at `p#platformAdminsCount`:

`5 مسؤول منصة · كل مسؤول يرى الشركات المسندة له فقط.`

The leading number is runtime data. V1.22 translates only the surrounding static summary while preserving the count.

Expected English form:
`5 platform admins · each admin sees only their assigned companies.`

Expected Arabic form remains:
`5 مسؤول منصة · كل مسؤول يرى الشركات المسندة له فقط.`

Do not translate names, emails, dates, IDs, paths, tenant/product/plan values, role/runtime values, or other domain/runtime data.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_21_PLATFORM_ADMINS_AR_FULL_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_22.py`

Run it twice.

First run must print:
`Applied Super Admin Bilingual V1.22 Platform Admins EN count closure runtime.`

Second run must be no-op:
`Super Admin bilingual V1.22 Platform Admins EN count closure already applied; no changes made.`

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
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_22_PLATFORM_ADMINS_EN_COUNT_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V122`
- `/super-admin/bilingual-v122.js`
- `superadmin-bilingual-v122`

If any marker is missing: STOP.

## Restart / readiness
Only after all static/build/dist gates pass:

`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds. Do not fail on a fixed short sleep.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v122.js?v=superadmin-bilingual-v122`

Expected:
- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V122`

## Regression gates
Fresh browser context, cache disabled.

Re-run:
- Users EN / AR
- Overview EN / AR
- Companies EN / AR
- Tenant Details EN / AR

Any regression = STOP.

## Platform Admins AR regression
Open `#platform-admins` in Arabic:
- `lang="ar"`
- `dir="rtl"`

Must still contain:
- `إدارة حسابات مسؤولي المنصة وتوزيع الشركات`
- `إدارة المنصة`
- `+ إضافة مسؤول`
- dynamic summary matching: `N مسؤول منصة · كل مسؤول يرى الشركات المسندة له فقط.`

Expected:
`PLATFORM ADMINS AR STATIC UI: NONE FOUND`

## Platform Admins EN closure gate
Switch to English:
- `lang="en"`
- `dir="ltr"`

Must contain:
- `PLATFORM ADMINISTRATION`
- `Manage Platform Admin accounts and company assignments`
- `+ Add Admin`
- dynamic summary matching: `N platform admins · each admin sees only their assigned companies.`

Explicitly forbid in English mode:
- `مسؤول منصة · كل مسؤول يرى الشركات المسندة له فقط.`
- any mixed Arabic/English form of that summary

Inspect:
- visible text
- placeholders
- title
- aria-label

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
RUNTIME V122:
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
