# TCRMMT Super Admin Bilingual V1.23 — Platform Admins EN Full Page Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_23.py` to `/var/www/TCRMMT`.

V1.22 passed runtime/build, all regression gates, Platform Admins AR, and the V1.22 dynamic English count closure. The V1.22 full-page raw scan then proved the remaining Platform Admins EN untranslated static UI set.

V1.23 closes the complete genuine static set evidenced in that scan:
- `إجمالي المسؤولين` → `Total admins`
- `كل حسابات Platform Administration` → `All Platform Admin accounts`
- `المسؤولون النشطون` → `Active admins`
- `حسابات متاحة لتسجيل الLogin` → `Accounts available for login`
- `شركات غير مسندة` → `Unassigned companies`
- `تحتاج ربطها بمسؤول منصة` → `Need assignment to a platform admin`
- `دليل مسؤولي المنصة` → `Platform Admin Directory`
- `الحسابات، الشركات المسندة، آخر Login والحالة.` → `Accounts, assigned companies, last login, and status.`
- `صلاحيات مركزية` → `Central permissions`
- `المسؤول` → `Admin`
- `أنشأه` → `Created by`
- `غير مسند لأي شركة` → `Not assigned to any company`
- `تعديل وربط الشركات` → `Edit & assign companies`

Do not translate person names, company names, emails, dates, IDs, paths, tenant/product/plan values, row role/runtime values, or other runtime/domain data.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_22_PLATFORM_ADMINS_EN_COUNT_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_23.py`

Run twice.
First run must print:
`Applied Super Admin Bilingual V1.23 Platform Admins EN full-page closure runtime.`

Second run must be no-op:
`Super Admin bilingual V1.23 Platform Admins EN full-page closure already applied; no changes made.`

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
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_23_PLATFORM_ADMINS_EN_FULL_PAGE_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V123`
- `/super-admin/bilingual-v123.js`
- `superadmin-bilingual-v123`

If any marker is missing: STOP.

## Restart / readiness
Only after all static/build/dist gates pass:
`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v123.js?v=superadmin-bilingual-v123`

Expected:
- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V123`

## Regression gates
Fresh browser context, cache disabled.

Re-run:
- Users EN / AR
- Overview EN / AR
- Companies EN / AR
- Tenant Details EN / AR

Any regression = STOP.

## Platform Admins AR
Verify Arabic still passes with:
- `إدارة المنصة`
- `إدارة حسابات مسؤولي المنصة وتوزيع الشركات`
- `+ إضافة مسؤول`
- `N مسؤول منصة · كل مسؤول يرى الشركات المسندة له فقط.`

Also verify the Platform Admin stats/table remain fully Arabic with no ordinary English static leakage.

Expected:
`PLATFORM ADMINS AR STATIC UI: NONE FOUND`

## Platform Admins EN Full Page Gate
Open `#platform-admins`, switch to English and verify:
- `lang="en"`
- `dir="ltr"`

Required top content:
- `PLATFORM ADMINISTRATION`
- `Manage Platform Admin accounts and company assignments`
- `+ Add Admin`
- `N platform admins · each admin sees only their assigned companies.`

Required full-page static values:
- `Total admins`
- `All Platform Admin accounts`
- `Active admins`
- `Accounts available for login`
- `Unassigned companies`
- `Need assignment to a platform admin`
- `Platform Admin Directory`
- `Accounts, assigned companies, last login, and status.`
- `Central permissions`
- `Admin`
- `Created by`
- `Not assigned to any company`
- `Edit & assign companies`

Explicitly forbid the V1.22 raw static leaks:
- `إجمالي المسؤولين`
- `كل حسابات Platform Administration`
- `المسؤولون النشطون`
- `حسابات متاحة لتسجيل الLogin`
- `شركات غير مسندة`
- `تحتاج ربطها بمسؤول منصة`
- `دليل مسؤولي المنصة`
- `الحسابات، الشركات المسندة، آخر Login والحالة.`
- `صلاحيات مركزية`
- `المسؤول`
- `أنشأه`
- `غير مسند لأي شركة`
- `تعديل وربط الشركات`

Scan:
- visible text
- placeholders
- title
- aria-label

Exclude runtime/data:
- person/company names
- emails
- dates
- IDs
- paths
- tenant/product/plan values
- role/runtime values
- runtime/domain data

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
RUNTIME V123:
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
