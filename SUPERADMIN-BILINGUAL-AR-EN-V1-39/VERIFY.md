# TCRMMT Super Admin Bilingual V1.39 — GitHub Sync AR Safe Cleanup Option Closure

## Scope

Apply only `apply_superadmin_bilingual_v1_39.py` to `/var/www/TCRMMT`.

Evidence basis: V1.38 passed apply/static gates/restart/runtime, Users EN/AR, Overview EN/AR, Companies EN/AR, Tenant Details EN/AR, Platform Admins EN/AR, Activity EN/AR, Audit Log EN/AR, and GitHub Sync EN. GitHub Sync AR then stopped at the first genuine ordinary untranslated static UI:

- selector: `#githubAction option[value="cleanup"]`
- current AR text: `Safe Cleanup`
- canonical AR text: `إلغاء آمن`

`Pull`, repository/branch/SHA/PAT/URLs/IPs/timestamps/event metadata and other technical/runtime values are excluded and must not be translated by this patch.

## Safety

Do not manually edit source, reset/clean/restore, change DB/migrations/Nginx, restart unrelated PM2 services, commit, or push.

Only this tracked file may change:

`server/superAdminUiPolish.ts`

## Apply

```bash
cd /var/www/TCRMMT
git status --short
python3 apply_superadmin_bilingual_v1_39.py
python3 apply_superadmin_bilingual_v1_39.py
```

Expected first run:

`Applied Super Admin Bilingual V1.39 GitHub Sync AR Safe Cleanup option closure runtime.`

Expected second run:

`Super Admin bilingual V1.39 GitHub Sync AR Safe Cleanup option closure already applied; no changes made.`

## Static gates

Run:

```bash
git diff --check
npm run check
npm run build
```

All must PASS.

Verify `dist/index.js` contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_39_GITHUB_SYNC_AR_SAFE_CLEANUP_OPTION_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V139`
- `/super-admin/bilingual-v139.js`
- `superadmin-bilingual-v139`

## Restart / stale guard

Only after all static gates PASS:

```bash
pm2 restart tamiyouz-crm
```

Restart no other service. Prove the new process start time is later than current `dist/index.js` mtime. If stale, STOP.

Poll port `3002` for up to 90 seconds.

## Runtime asset gate

Verify Direct and Public three times each:

`/super-admin/bilingual-v139.js?v=superadmin-bilingual-v139`

Require:
- HTTP 200
- JavaScript Content-Type
- Cache-Control no-store
- body contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V139`
- no HTML fallback

Any failure = STOP.

## Fresh browser regression

Use fresh authenticated browser context, cache disabled/cache-busted.

Re-run EN then AR:

1. Users
2. Overview
3. Companies
4. Tenant Details
5. Platform Admins
6. Activity
7. Audit Log
8. GitHub Sync

Preserve all prior gates.

### GitHub Sync EN

`#githubAction option[value="cleanup"]` must equal:

`Safe Cleanup`

Expected:

`GITHUB SYNC EN STATIC UI: NONE FOUND`

### GitHub Sync AR — primary V1.39 gate

Require `lang=ar`, `dir=rtl`.

`#githubAction option[value="cleanup"]` must equal exactly:

`إلغاء آمن`

Forbidden:

`Safe Cleanup`

Do not flag `Pull` or other documented technical/runtime/domain values.

Expected:

`GITHUB SYNC AR STATIC UI: NONE FOUND`

## Continue Full Audit

Only if all regressions PASS, continue EN then AR:

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

At the first genuine ordinary untranslated static UI: STOP immediately. Do not fix manually. Capture language, page/hash, exact text, untranslated segment, selector/attribute, raw browser finding, and screenshot.

Create:

`TCRMMT_V139_Evidence.zip`

No commit. No push.

## Session handoff

Put/upload the final report and Evidence ZIP inside the user's ChatGPT Session named exactly:

`TCRMMMT`
