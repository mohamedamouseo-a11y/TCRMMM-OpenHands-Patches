# TCRMMT Super Admin Bilingual V1.36 — Users EN Dynamic Account Count Closure

## Scope

Apply only `apply_superadmin_bilingual_v1_36.py` to `/var/www/TCRMMT`.

Evidence basis: V1.35 passed source/build/runtime gates, but fresh Browser QA stopped at Users EN because `#platformUsersPager > .muted` rendered `17 حساب` instead of `17 accounts`.

V1.36 preserves the runtime numeric count and translates only the static account noun on `#users`.

## Safety

Do not manually edit source, reset/clean/restore tracked files, modify DB/migrations/Nginx, restart unrelated PM2 services, commit, or push.

Only this tracked file may change:

`server/superAdminUiPolish.ts`

## Apply

```bash
cd /var/www/TCRMMT
git status --short
python3 apply_superadmin_bilingual_v1_36.py
python3 apply_superadmin_bilingual_v1_36.py
```

Expected first run:

`Applied Super Admin Bilingual V1.36 Users EN dynamic account count closure runtime.`

Expected second run:

`Super Admin bilingual V1.36 Users EN dynamic account count closure already applied; no changes made.`

## Static gates

Run:

```bash
git diff --check
npm run check
npm run build
```

All must PASS.

Verify dist contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_36_USERS_EN_DYNAMIC_ACCOUNT_COUNT_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V136`
- `/super-admin/bilingual-v136.js`
- `superadmin-bilingual-v136`

## Restart

Only after all static gates PASS:

```bash
pm2 restart tamiyouz-crm
```

Restart no other service.

Capture the new PID and prove its start time is after current `dist/index.js` mtime. If stale, STOP.

Poll port 3002 for up to 90 seconds.

## Runtime asset gate

Verify Direct and Public three times:

`/super-admin/bilingual-v136.js?v=superadmin-bilingual-v136`

Require:

- HTTP 200
- JavaScript Content-Type
- Cache-Control no-store
- body contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V136`
- no HTML fallback

## Fresh Browser QA

Use fresh/cache-busted browser context with cache disabled.

### Users EN primary V1.36 gate

Open `#users` in English after data load.

Require:

- `lang=en`
- `dir=ltr`
- `#platformUsersPager > .muted` equals `<runtime-count> accounts` for the current count.
- With the current evidence dataset, expected exact value is `17 accounts`.

Forbid:

- `<runtime-count> حساب`
- specifically `17 حساب`

The number itself is runtime/data and must remain unchanged.

Expected line:

`USERS EN STATIC UI: NONE FOUND`

### Users AR

Switch to Arabic and verify the same pager uses:

`<runtime-count> حساب`

With current evidence, expected `17 حساب`.

Expected:

`USERS AR STATIC UI: NONE FOUND`

## Re-run all regressions

If Users EN/AR PASS, continue EN then AR:

1. Overview
2. Companies
3. Tenant Details
4. Platform Admins
5. Activity
6. Audit Log
7. GitHub Sync

Keep all prior V1.34/V1.35 canonical gates.

For GitHub Sync EN require:

- `Review platform source and execute sync safely`
- `All operations`
- `Safe cancel`
- `GITHUB SYNC EN STATIC UI: NONE FOUND`

For GitHub Sync AR require:

- `مراجعة مصدر المنصة وتنفيذ المزامنة بأمان`
- `كل العمليات`
- `إلغاء آمن`
- `GITHUB SYNC AR STATIC UI: NONE FOUND`

Do not treat runtime/domain/audit data as translation blockers: names, emails, dates/timestamps, IDs, paths, repository/branch/SHA values, URLs, IPs, roles, audit event names, technical errors, plan/runtime values.

## Continue Full Audit

Only if all regressions pass, continue EN then AR:

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

At the first genuine ordinary untranslated static UI: STOP immediately; do not fix manually. Record language, page/hash, exact text, untranslated segment, selector/attribute, raw browser finding, and screenshot.

## Evidence

Create:

`TCRMMT_V136_Evidence.zip`

No commit. No push.

## Session handoff

Put/upload the final report and Evidence ZIP inside the user's ChatGPT Session named exactly:

`TCRMMMT`
