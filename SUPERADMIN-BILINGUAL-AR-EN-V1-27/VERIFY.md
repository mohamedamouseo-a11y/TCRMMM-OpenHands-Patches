# TCRMMT Super Admin Bilingual V1.27 — Audit Log AR Mixed H2 Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_27.py` to `/var/www/TCRMMT`.

V1.26 passed apply/build/runtime, all prior regression gates, and Audit Log EN. Audit Log AR then stopped at one genuine ordinary mixed static H2:
- `أمان & Audit Log` → `الأمان وسجل التدقيق`

V1.27 closes only this evidenced Arabic canonicalization gap. Do not translate runtime event names, emails, IPs, dates/timestamps, IDs, paths, person/company names, plan/product values, or other runtime/domain data.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_26_AUDIT_LOG_EN_MIXED_H2_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_27.py`

Run twice.

First run:
`Applied Super Admin Bilingual V1.27 Audit Log AR mixed H2 closure runtime.`

Second run:
`Super Admin bilingual V1.27 Audit Log AR mixed H2 closure already applied; no changes made.`

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
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_27_AUDIT_LOG_AR_MIXED_H2_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V127`
- `/super-admin/bilingual-v127.js`
- `superadmin-bilingual-v127`

## Restart / readiness
Only after all static/build/dist gates pass:
`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v127.js?v=superadmin-bilingual-v127`

Expected:
- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V127`

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

## Audit Log EN
Open `#audit` in English.

Required:
- `Security & Audit Log`
- `Export Log`
- `Action Type`
- `Event`
- `Recorded Events`
- `Latest administrative operations ordered from newest to oldest`

Explicitly forbid:
- `أمان & Audit Log`
- `الأمان وسجل التدقيق`

Expected:
`AUDIT LOG EN STATIC UI: NONE FOUND`

## Audit Log AR
Switch to Arabic and verify `lang="ar"`, `dir="rtl"`.

Required canonical:
- `الأمان وسجل التدقيق`
- `تصدير السجل`
- `نوع الإجراء`
- `الحدث`
- `الأحداث المسجلة`
- `آخر العمليات الإدارية مرتبة من الأحدث إلى الأقدم`

Explicitly forbid:
- `أمان & Audit Log`
- `Security & Audit Log`

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

On the first genuine ordinary untranslated static UI:
**STOP immediately. Do not fix manually.**

Record language, page/hash, exact text, untranslated segment, selector/attribute, raw browser finding, and screenshot.

Send ZIP Evidence and final report.

No commit or push.
