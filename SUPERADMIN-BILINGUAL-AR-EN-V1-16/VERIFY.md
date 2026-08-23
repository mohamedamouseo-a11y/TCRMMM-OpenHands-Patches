# Super Admin Bilingual V1.16 — Users AR Header Closure

Target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`

## Purpose

V1.15 passed Runtime, lifecycle, persistence, Overview EN/AR, Companies EN/AR, and Tenant Details EN/AR.
The first Full Audit failure was Users AR. Raw evidence contained only two ordinary untranslated static strings:

- `USERS & ACCESS`
- `Central Users`

Other English-containing findings were permitted user names, integrations/products, or technical/queue/source values.

V1.16 adds exact bidirectional mappings for those two Users strings only and bumps the standalone runtime asset/version to V116.

## Apply

Run outside the worktree:

```bash
python3 apply_superadmin_bilingual_v1_16.py
python3 apply_superadmin_bilingual_v1_16.py
```

Second run must be no-op.

## Required static checks

```bash
git diff --check
npm run check
npm run build
```

Only this production source may be modified:

```text
server/superAdminUiPolish.ts
```

## Dist Gate

Before restart, `dist/index.js` must contain:

```text
SUPER_ADMIN_BILINGUAL_AR_EN_V1_16_USERS_AR_HEADER_CLOSURE
SUPER_ADMIN_BILINGUAL_RUNTIME_V116
/super-admin/bilingual-v116.js
superadmin-bilingual-v116
```

## Runtime

Restart only:

```bash
pm2 restart tamiyouz-crm
```

Asset:

```text
/super-admin/bilingual-v116.js?v=superadmin-bilingual-v116
```

Must return JavaScript 200 with no-store and `SUPER_ADMIN_BILINGUAL_RUNTIME_V116`.

## Browser gates

Regression:
- Overview EN/AR: NONE FOUND
- Companies EN/AR: NONE FOUND
- Tenant Details EN/AR: NONE FOUND

Users AR must show:
- `المستخدمون والصلاحيات`
- `المستخدمون المركزيون`

and must not show:
- `USERS & ACCESS`
- `Central Users`

Then run Users EN and continue Full Audit from:
Platform Admins, Activity, Audit Log, GitHub Sync, Evolution API, Tara APIs, Plans Catalog, Plan Editor, Company Overrides, Commercial, Billing, Subscriptions, Settings, Source Code.

Stop at the first ordinary untranslated static finding. Do not fix it manually.

No commit/push/reset/clean/restore/manual code edits.
