# TCRMMT Super Admin Bilingual V1.26 — Audit Log EN Mixed H2 Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_26.py` to `/var/www/TCRMMT`.

V1.25 passed apply/build/runtime and all prior regression gates. Its six required Audit Log EN values were present, but browser evidence found one remaining genuine ordinary static H2:

- `أمان & Audit Log` → `Security & Audit Log`

The Arabic segment `أمان` is static UI. V1.26 closes only this evidenced post-translation mixed H2. Do not translate runtime event names, emails, IPs, dates/timestamps, IDs, paths, person/company names, plan/product values, or other runtime/domain data.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_25_AUDIT_LOG_EN_FULL_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_26.py`

Run twice.

First run must print:
`Applied Super Admin Bilingual V1.26 Audit Log EN mixed H2 closure runtime.`

Second run must be no-op:
`Super Admin bilingual V1.26 Audit Log EN mixed H2 closure already applied; no changes made.`

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
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_26_AUDIT_LOG_EN_MIXED_H2_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V126`
- `/super-admin/bilingual-v126.js`
- `superadmin-bilingual-v126`

## Restart / readiness
Only after all static/build/dist gates pass:
`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v126.js?v=superadmin-bilingual-v126`

Expected:
- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V126`

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
Open `#audit` in English and verify `lang="en"` and `dir="ltr"`.

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
- `تصدير السجل`
- `نوع الإجراء`
- `الحدث`
- `الأحداث المسجلة`
- `آخر العمليات الإدارية مرتبة من الأحدث إلى الأقدم`

Scan visible text, placeholders, title, and aria-label.

Expected:
`AUDIT LOG EN STATIC UI: NONE FOUND`

## Audit Log AR gate
Switch to Arabic and verify `lang="ar"` and `dir="rtl"`.

Required canonical Arabic values:
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

Send ZIP Evidence and final report.

No commit or push.
