# TCRMMT Super Admin Bilingual V1.37 — GitHub Sync EN Audit Action Placeholder Closure

## Scope

Apply only `apply_superadmin_bilingual_v1_37.py` to `/var/www/TCRMMT`.

Evidence basis: V1.36 passed apply/no-op, static gates, build, PM2 stale guard, Direct/Public V136 runtime asset, Users EN/AR, Overview EN/AR, Companies EN/AR, Tenant Details EN/AR, Platform Admins EN/AR, Activity EN/AR, and Audit Log EN/AR. Browser QA then stopped at the first genuine ordinary untranslated static UI in GitHub Sync EN:

- selector: `#auditAction`
- attribute: `placeholder`
- current EN value: `مثل subscription أو github.sync`
- required EN value: `e.g. subscription or github.sync`

This is static UI copy. The technical/event examples `subscription` and `github.sync` remain unchanged.

V1.37 adds a post-render attribute override for this exact field and preserves canonical Arabic in AR mode.

## Safety

Do not manually edit source. Do not reset, clean, restore, modify DB/migrations/Nginx, restart unrelated PM2 services, commit, or push.

Only this tracked file may change:

`server/superAdminUiPolish.ts`

## Apply

```bash
cd /var/www/TCRMMT
git status --short
python3 apply_superadmin_bilingual_v1_37.py
python3 apply_superadmin_bilingual_v1_37.py
```

Expected first run:

`Applied Super Admin Bilingual V1.37 GitHub Sync EN audit action placeholder closure runtime.`

Expected second run:

`Super Admin bilingual V1.37 GitHub Sync EN audit action placeholder closure already applied; no changes made.`

Confirm the only tracked modified file remains `server/superAdminUiPolish.ts`.

## Static gates

```bash
git diff --check
npm run check
npm run build
```

All must PASS.

Verify `dist/index.js` contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_37_GITHUB_SYNC_EN_AUDIT_ACTION_PLACEHOLDER_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V137`
- `/super-admin/bilingual-v137.js`
- `superadmin-bilingual-v137`

## Restart and stale-process guard

Only after all static gates PASS:

```bash
pm2 restart tamiyouz-crm
```

Restart no other service.

Capture the new PID and prove its start time is later than the current `dist/index.js` mtime. If stale, STOP; do not edit or rebuild.

Poll port `3002` for up to 90 seconds.

## Runtime asset gate

Verify Direct and Public three times each:

`/super-admin/bilingual-v137.js?v=superadmin-bilingual-v137`

Required every time:

- HTTP 200
- JavaScript Content-Type
- `Cache-Control` no-store
- body contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V137`
- no HTML fallback

Any failure = STOP.

## Fresh Browser QA

Use a fresh authenticated browser context, cache disabled, and a cache-busted URL.

Re-run regressions EN then AR:

1. Users
2. Overview
3. Companies
4. Tenant Details
5. Platform Admins
6. Activity
7. Audit Log

Keep all previously established gates, including:

- Users EN pager: `<runtime-count> accounts`
- Users AR pager: `<runtime-count> حساب`
- Companies/Tenant Details operational and technical values remain DATA exclusions.

### GitHub Sync EN — primary V1.37 gate

Open `#github` in English and require:

- `lang=en`
- `dir=ltr`
- `#auditAction` placeholder exactly: `e.g. subscription or github.sync`

Forbid:

- `مثل subscription أو github.sync`

Also confirm the previous GitHub Sync EN gates still pass, including:

- `Review platform source and execute sync safely`
- `All operations`
- `Safe cancel`

Expected:

`GITHUB SYNC EN STATIC UI: NONE FOUND`

### GitHub Sync AR

Switch to Arabic and require:

- `lang=ar`
- `dir=rtl`
- `#auditAction` placeholder exactly: `مثل subscription أو github.sync`

Also confirm canonical Arabic GitHub Sync labels remain present.

Expected:

`GITHUB SYNC AR STATIC UI: NONE FOUND`

Do not flag runtime/domain/audit data such as names, emails, dates/timestamps, IDs, repo/branch/SHA, URLs, IPs, roles, event names/metadata, technical errors, plan/runtime values, or actual audit payload values.

## Continue Full Audit

Only if all regressions and GitHub Sync EN/AR PASS, continue EN then AR:

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

At the first genuine ordinary untranslated static UI, STOP immediately. Do not fix it manually.

Capture:

- language
- page/hash
- exact text
- untranslated segment
- selector/attribute
- raw browser finding
- screenshot

## Evidence

Create:

`TCRMMT_V137_Evidence.zip`

Include apply/no-op, source scope, static gates, build markers, PM2 restart/stale proof, Direct/Public asset checks, regression results, GitHub Sync EN/AR results, Full Audit progress, first finding if any, screenshots, and final report.

No commit. No push.

## Session handoff

Put/upload the final report and Evidence ZIP inside the user's ChatGPT Session named exactly:

`TCRMMMT`
