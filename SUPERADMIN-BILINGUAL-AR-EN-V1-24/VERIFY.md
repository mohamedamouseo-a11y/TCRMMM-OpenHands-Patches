# TCRMMT Super Admin Bilingual V1.24 — Activity EN Header / Last Activity Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_24.py` to `/var/www/TCRMMT`.

V1.23 passed runtime/build and all regression gates through Platform Admins EN/AR. The first genuine Full Audit blocker was then proven on Activity EN:

- `آخر الأنشطة` — static page heading
- `آخر نشاط: <runtime timestamp>` — static label + runtime timestamp

V1.24 translates the static portions only:
- `آخر الأنشطة` → `Latest Activity`
- `آخر نشاط: <timestamp>` → `Last activity: <same timestamp>`

The timestamp bytes are runtime data and must remain unchanged.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_23_PLATFORM_ADMINS_EN_FULL_PAGE_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_24.py`

Run it twice.
First run must print:
`Applied Super Admin Bilingual V1.24 Activity EN header/last-activity closure runtime.`

Second run must be no-op:
`Super Admin bilingual V1.24 Activity EN header/last-activity closure already applied; no changes made.`

## Safety
No manual source edits, reset/clean/restore, commit/push, DB/migrations, Nginx changes, or unrelated PM2 changes.

## Static gates
Only `server/superAdminUiPolish.ts` may change.

Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

## Dist gate
Before restart, `dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_24_ACTIVITY_EN_HEADER_LAST_ACTIVITY_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V124`
- `/super-admin/bilingual-v124.js`
- `superadmin-bilingual-v124`

If any marker is missing: STOP.

## Restart / readiness
Only after all gates pass:
`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v124.js?v=superadmin-bilingual-v124`

Expected:
- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V124`

## Regression gates
Fresh browser context, cache disabled.

Re-run:
- Users EN / AR
- Overview EN / AR
- Companies EN / AR
- Tenant Details EN / AR
- Platform Admins EN / AR

Any regression = STOP.

## Activity EN gate
Open `#activity` in English and verify:
- `lang="en"`
- `dir="ltr"`
- heading: `Latest Activity`
- each activity-card label begins with `Last activity:`
- timestamps remain runtime values and are not translated/rewritten

Explicitly forbid ordinary static leakage:
- `آخر الأنشطة`
- `آخر نشاط:`

Scan:
- visible text
- placeholders
- title
- aria-label

Expected:
`ACTIVITY EN STATIC UI: NONE FOUND`

## Activity AR gate
Switch to Arabic and verify:
- `lang="ar"`
- `dir="rtl"`
- heading: `آخر الأنشطة`
- activity labels begin with `آخر نشاط:`
- no ordinary English static leakage from the V1.24 canonical values

Expected:
`ACTIVITY AR STATIC UI: NONE FOUND`

## Continue remaining Full Audit
Only if Activity EN and AR both PASS, continue EN + AR:

1. Audit Log
2. GitHub Sync
3. Evolution API
4. Tara APIs
5. Plans Catalog
6. Plan Editor
7. Company Overrides
8. Commercial
9. Billing
10. Subscriptions
11. Settings
12. Source Code

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
RUNTIME V124:
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
ACTIVITY EN:
ACTIVITY AR:
NEXT TRANSLATION BLOCKER:
UNTRANSLATED STATIC UI:
```

Send ZIP Evidence and stop.

No commit or push.
