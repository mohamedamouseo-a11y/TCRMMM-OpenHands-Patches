# TCRMMT Super Admin Bilingual V1.34 — Tenant Details EN Provisioning Static Closure

## Scope

Apply only `apply_superadmin_bilingual_v1_34.py` to `/var/www/TCRMMT`.

Evidence basis: V1.33 passed stale-runtime restart, V133 Direct/Public asset, Users EN/AR, Overview EN/AR, and Companies EN/AR. Browser QA then stopped at the first genuine ordinary untranslated static UI inside Tenant Details EN.

This patch closes only the evidence-backed ordinary static provisioning copy in the Tenant Details surface. Do not translate runtime/domain/technical data such as company names, emails, paths, provisioning status values, dates/timestamps, IDs, plan values, numeric counters, or raw technical errors.

## Safety

Do not manually edit source, reset/clean/restore tracked files, modify DB/migrations/Nginx, restart unrelated PM2 services, commit, or push.

Only this tracked file may change:

`server/superAdminUiPolish.ts`

## Apply

Before apply:

```bash
cd /var/www/TCRMMT
git status --short
```

Run the official patch twice.

First run:

`Applied Super Admin Bilingual V1.34 Tenant Details EN provisioning static closure runtime.`

Second run:

`Super Admin bilingual V1.34 Tenant Details EN provisioning static closure already applied; no changes made.`

After the second run, confirm only `server/superAdminUiPolish.ts` is modified.

## Static gates

Run:

```bash
git diff --check
npm run check
npm run build
```

All must PASS.

Verify the built bundle contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_34_TENANT_DETAILS_EN_PROVISIONING_STATIC_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V134`
- `/super-admin/bilingual-v134.js`
- `superadmin-bilingual-v134`

## Restart and stale-process guard

Only after all static gates PASS:

```bash
pm2 restart tamiyouz-crm
```

Restart no other service.

Capture the new PID and prove the new process start time is later than the current `dist/index.js` mtime. If stale, STOP and report; do not edit code.

Poll port `3002` for up to 90 seconds.

## Runtime asset gate

Verify Direct and Public:

`/super-admin/bilingual-v134.js?v=superadmin-bilingual-v134`

Required:
- HTTP 200
- JavaScript Content-Type
- `Cache-Control` no-store
- body contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V134`

Repeat Direct/Public 3 times. HTML fallback is FAIL/STOP.

## Fresh Browser

Use a fresh browser context with cache disabled/cache-busted URL.

Re-run regression gates, EN then AR:

1. Users
2. Overview
3. Companies
4. Tenant Details
5. Platform Admins
6. Activity
7. Audit Log
8. GitHub Sync

### Companies regression

EN `button.retryProvisionBtn` = `Retry provisioning`

AR `button.retryProvisionBtn` = `إعادة التجهيز`

Operational provisioning statuses remain DATA and are not translation blockers.

### Tenant Details EN — primary V1.34 gate

Open the same Tenant Details drawer under `#tenants` in English.

Require:

- `Company provisioning failed`
- `The provisioning worker runs as an independent PM2 service and processes the queue automatically.`
- `Job ID`
- `Attempts`
- `Retry provisioning`
- `Retry safely reuses the same job and does not create a duplicate company.`

Forbid:

- `تعذر تجهيز الشركة`
- `عامل التجهيز يعمل كخدمة PM2 مستقلة ويعالج قائمة الانتظار تلقائيًا.`
- `رقم المهمة`
- `المحاولات`
- `إعادة محاولة التجهيز`
- `إعادة المحاولة تستخدم نفس المهمة بأمان ولا تنشئ شركة مكررة.`

Do not flag company/person names, emails, paths, `فشل التجهيز` / `فشلت` when rendered as operational provisioning status, dates/timestamps, IDs/numbers, plan/runtime values, or raw technical errors such as `tenant_schema_manifest_version_invalid:...`.

Expected:

`TENANT DETAILS EN STATIC UI: NONE FOUND`

### Tenant Details AR

Switch to Arabic and verify the same ordinary static copy is canonical Arabic:

- `تعذر تجهيز الشركة`
- `عامل التجهيز يعمل كخدمة PM2 مستقلة ويعالج قائمة الانتظار تلقائيًا.`
- `رقم المهمة`
- `المحاولات`
- `إعادة محاولة التجهيز`
- `إعادة المحاولة تستخدم نفس المهمة بأمان ولا تنشئ شركة مكررة.`

Expected:

`TENANT DETAILS AR STATIC UI: NONE FOUND`

## Continue full audit

If all regression gates through GitHub Sync EN/AR PASS, continue:

1. Evolution API EN / AR
2. Tara APIs EN / AR
3. Plans Catalog EN / AR
4. Plan Editor EN / AR
5. Company Overrides EN / AR
6. Commercial EN / AR
7. Billing EN / AR
8. Subscriptions EN / AR
9. Settings EN / AR
10. Source Code EN / AR

At the first genuine ordinary untranslated static UI: STOP immediately; do not fix manually. Capture language, page/hash, exact text, untranslated segment, selector/attribute, raw browser finding, and screenshot.

Create `TCRMMT_V134_Evidence.zip`.

No commit. No push.

## Session handoff

Put/upload the final report and Evidence ZIP inside the user's ChatGPT Session named exactly:

`TCRMMMT`
