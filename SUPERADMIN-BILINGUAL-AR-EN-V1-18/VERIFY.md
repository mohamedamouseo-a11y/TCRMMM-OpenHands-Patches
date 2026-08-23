# TCRMMT Super Admin Bilingual V1.18 — Users Mixed Header Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_18.py` to `/var/www/TCRMMT`.

This patch closes the complete genuine static Users EN blockers evidenced after V1.17 runtime recovery:
- `إدارة موحدة لAll companies` → `Unified management for all companies`
- `آخر Login` → `Last Login`
- `بيانات الLogin` → `Login Details`

It also canonicalizes the Arabic forms to:
- `إدارة موحدة لكل الشركات`
- `آخر تسجيل دخول`
- `بيانات تسجيل الدخول`

Do not translate tenant/company/user names, emails, dates, IDs, or other runtime data.

## Preconditions
Required source markers:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_STARTUP_HOTFIX`

## Apply
Run twice. First run must apply; second run must be no-op.

## Static gates
Only `server/superAdminUiPolish.ts` may change.
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

Dist must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_18_USERS_MIXED_HEADER_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V118`
- `/super-admin/bilingual-v118.js`

## Runtime gates
Restart only `tamiyouz-crm` after successful build.
Use readiness polling for port `3002` for up to 90 seconds; do not use a fixed short sleep as a failure gate.
Verify direct and public `/super-admin` and `/super-admin/bilingual-v118.js?v=superadmin-bilingual-v118` return HTTP 200 and the runtime asset has `no-store` and `SUPER_ADMIN_BILINGUAL_RUNTIME_V118`.

## Browser QA
Fresh browser context, cache disabled.

### Users EN
Must contain no ordinary untranslated Arabic static UI. Specifically forbid:
- `إدارة موحدة لAll companies`
- `إدارة موحدة`
- `آخر Login`
- `آخر LOGIN`
- `بيانات الLogin`
- `بيانات الLOGIN`

Expected:
- `Unified management for all companies`
- `Last Login`
- `Login Details`

### Users AR
Verify canonical Arabic UI and no ordinary English static leakage:
- `إدارة موحدة لكل الشركات`
- `آخر تسجيل دخول`
- `بيانات تسجيل الدخول`

Then re-run regressions:
- Overview EN/AR
- Companies EN/AR
- Tenant Details EN/AR

If all pass, continue remaining Full Audit EN+AR:
- Platform Admins
- Activity
- Audit Log
- GitHub Sync
- Evolution API
- Tara APIs
- Plans Catalog
- Plan Editor
- Company Overrides
- Commercial
- Billing
- Subscriptions
- Settings
- Source Code

Stop on the first genuine ordinary untranslated static finding. Record exact text, page, language, selector/attribute, raw browser findings, and screenshot. Do not manually fix it.

## Safety
No reset/clean/restore/manual source edits/commit/push. No Nginx, DB, migration, or unrelated PM2 changes.
