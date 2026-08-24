# TCRMMT Super Admin Bilingual V1.25 — Audit Log EN Full Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_25.py` to `/var/www/TCRMMT`.

V1.24 passed runtime/build, all previous regression gates, Activity EN and Activity AR. The V1.24 Full Audit then stopped at the first genuine ordinary untranslated static UI set in **Audit Log EN**.

V1.25 closes the complete six-string static set evidenced there:
- `الأمان وسجل التدقيق` → `Security & Audit Log`
- `تصدير السجل` → `Export Log`
- `نوع الإجراء` → `Action Type`
- `الحدث` → `Event`
- `الأحداث المسجلة` → `Recorded Events`
- `آخر العمليات الإدارية مرتبة من الأحدث إلى الأقدم` → `Latest administrative operations ordered from newest to oldest`

Do not translate runtime event names such as `super_admin.login`, emails, IP addresses, dates/timestamps, IDs, paths, person/company names, plan/product values, or other runtime/domain data.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_24_ACTIVITY_EN_HEADER_LAST_ACTIVITY_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_25.py`

Run it twice.
First run must print:
`Applied Super Admin Bilingual V1.25 Audit Log EN full closure runtime.`

Second run must be no-op:
`Super Admin bilingual V1.25 Audit Log EN full closure already applied; no changes made.`

## Safety
No manual source edits, reset, clean, restore, commit, push, DB/migration changes, Nginx changes, or unrelated PM2 changes.

## Static gates
Only `server/superAdminUiPolish.ts` may change.

Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

## Dist gate
Before restart, `dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_25_AUDIT_LOG_EN_FULL_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V125`
- `/super-admin/bilingual-v125.js`
- `superadmin-bilingual-v125`

## Restart / readiness
Only after all static/build/dist gates pass:
`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v125.js?v=superadmin-bilingual-v125`

Expected:
- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V125`

## Regression gates
Fresh browser context, cache disabled.

Re-run:
- Users EN / AR
- Overview EN / AR
- Companies EN / AR
- Tenant Details EN / AR
- Platform Admins EN / AR
- Activity EN / AR

Any regression = STOP.

## Audit Log EN full gate
Open `#audit` in English and verify:
- `lang="en"`
- `dir="ltr"`

Required static values:
- `Security & Audit Log`
- `Export Log`
- `Action Type`
- `Event`
- `Recorded Events`
- `Latest administrative operations ordered from newest to oldest`

Explicitly forbid:
- `الأمان وسجل التدقيق`
- `تصدير السجل`
- `نوع الإجراء`
- `الحدث`
- `الأحداث المسجلة`
- `آخر العمليات الإدارية مرتبة من الأحدث إلى الأقدم`

Scan visible text, placeholders, `title`, and `aria-label`.

Exclude runtime/data such as event names, emails, IPs, dates/timestamps, IDs, paths, person/company names, plan/product values, and runtime/domain data.

Expected:
`AUDIT LOG EN STATIC UI: NONE FOUND`

## Audit Log AR gate
Switch to Arabic and verify:
- `lang="ar"`
- `dir="rtl"`

Required canonical values:
- `الأمان وسجل التدقيق`
- `تصدير السجل`
- `نوع الإجراء`
- `الحدث`
- `الأحداث المسجلة`
- `آخر العمليات الإدارية مرتبة من الأحدث إلى الأقدم`

Expected:
`AUDIT LOG AR STATIC UI: NONE FOUND`

## Continue remaining Full Audit
Only if Audit Log EN and AR both PASS, continue EN + AR:
1. GitHub Sync
2. Evolution API
3. Tara APIs
4. Plans Catalog
5. Plan Editor
6. Company Overrides
7. Commercial
8. Billing
9. Subscriptions
10. Settings
11. Source Code

On the first genuine ordinary untranslated static UI: **STOP immediately. Do not fix manually.**

Record language, page/hash, exact text, untranslated segment, selector/attribute, raw browser finding, and screenshot.

Send ZIP Evidence and final report. No commit or push.
