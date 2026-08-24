# TCRMMT Super Admin Bilingual V1.28 — Activity EN View All Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_28.py` to `/var/www/TCRMMT`.

V1.27 passed static/build/runtime and all browser regressions through Activity AR. The V1.27 Activity EN regression then found one genuine ordinary static blocker:
- `#activityRefreshBtn`: `عرض الكل` → expected `View all`

V1.28 closes only that button label and adds the reverse Arabic canonicalization. Runtime timestamps and all runtime/domain data remain untouched.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_27_AUDIT_LOG_AR_MIXED_H2_CLOSURE`

## Apply
Run twice:
`python3 apply_superadmin_bilingual_v1_28.py`

First run must print:
`Applied Super Admin Bilingual V1.28 Activity EN View all closure runtime.`

Second run must be no-op:
`Super Admin bilingual V1.28 Activity EN View all closure already applied; no changes made.`

## Safety
No manual source edits, reset, clean, restore, commit, push, DB/migrations, Nginx changes, or unrelated PM2 changes.

## Static/build gates
Only `server/superAdminUiPolish.ts` may change.

Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

## Dist gate
Before restart `dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_28_ACTIVITY_EN_VIEW_ALL_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V128`
- `/super-admin/bilingual-v128.js`
- `superadmin-bilingual-v128`

## Restart/runtime
Only after gates PASS:
`pm2 restart tamiyouz-crm`

Poll port `3002` for up to 90 seconds.
Verify Direct/Public:
- `/super-admin`
- `/super-admin/bilingual-v128.js?v=superadmin-bilingual-v128`

Expected HTTP 200, JavaScript Content-Type, no-store, runtime marker V128.

## Regression gates
Fresh browser context, cache disabled. Re-run:
- Users EN / AR
- Overview EN / AR
- Companies EN / AR
- Tenant Details EN / AR
- Platform Admins EN / AR
- Activity AR / EN

Activity EN must have:
- `Latest Activity`
- `Last activity: <timestamp>` labels
- `#activityRefreshBtn` exactly `View all`
- no ordinary Arabic static leakage

Activity AR must have:
- `آخر الأنشطة`
- `آخر نشاط: <timestamp>` labels
- `#activityRefreshBtn` exactly `عرض الكل`
- no ordinary English static leakage

Any regression = STOP.

## Resume Audit Log
If all regressions PASS, verify Audit Log EN and AR again.

Audit Log EN required:
- `Security & Audit Log`
- `Export Log`
- `Action Type`
- `Event`
- `Recorded Events`
- `Latest administrative operations ordered from newest to oldest`
- no `أمان & Audit Log`

Audit Log AR required:
- `الأمان وسجل التدقيق`
- `تصدير السجل`
- `نوع الإجراء`
- `الحدث`
- `الأحداث المسجلة`
- `آخر العمليات الإدارية مرتبة من الأحدث إلى الأقدم`
- no `أمان & Audit Log`
- no ordinary English static leakage

Expected:
- `AUDIT LOG EN STATIC UI: NONE FOUND`
- `AUDIT LOG AR STATIC UI: NONE FOUND`

## Continue remaining Full Audit
Only if Audit Log EN/AR both PASS, continue EN + AR:
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

On first genuine ordinary untranslated static UI: STOP immediately. Do not fix manually.
Record language, page/hash, exact text, selector/attribute, raw finding, screenshot.

Send `TCRMMT_V128_Evidence.zip` and final report. No commit or push.
