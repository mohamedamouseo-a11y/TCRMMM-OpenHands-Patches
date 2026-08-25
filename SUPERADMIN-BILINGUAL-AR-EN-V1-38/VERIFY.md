# TCRMMT Super Admin Bilingual V1.38 — Audit Log EN Action Placeholder Final Runtime Pin

## Scope

Apply only `apply_superadmin_bilingual_v1_38.py` to `/var/www/TCRMMT`.

Evidence basis: V1.37 build/runtime passed. The Tenant Details skeleton issue was rechecked and classified transient; Tenant Details EN/AR then passed. The resumed QA stopped at the first genuine ordinary untranslated static UI in Audit Log EN: `#auditAction` placeholder remained `مثل subscription أو github.sync` while the page was `lang=en`, `dir=ltr`.

V1.37 already added the canonical placeholder to the legacy translation sweep. V1.38 pins the same attribute in the standalone bilingual runtime's final sweep so the later runtime cannot restore the Arabic source value while English is active.

Do not translate runtime/domain/audit data.

## Safety

Do not manually edit source, reset/clean/restore, modify DB/migrations/Nginx, restart unrelated services, commit, or push.

Only this tracked file may change:

`server/superAdminUiPolish.ts`

## Apply

```bash
cd /var/www/TCRMMT
git status --short
python3 apply_superadmin_bilingual_v1_38.py
python3 apply_superadmin_bilingual_v1_38.py
```

Expected first run:

`Applied Super Admin Bilingual V1.38 Audit Log EN action placeholder final runtime pin.`

Expected second run:

`Super Admin bilingual V1.38 Audit Log EN action placeholder final runtime pin already applied; no changes made.`

## Static gates

Run:

```bash
git diff --check
npm run check
npm run build
```

All must PASS.

Verify built output contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_38_AUDIT_LOG_EN_ACTION_PLACEHOLDER_FINAL_RUNTIME_PIN`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V138`
- `/super-admin/bilingual-v138.js`
- `superadmin-bilingual-v138`

## Restart / stale guard

Only after static gates PASS:

```bash
pm2 restart tamiyouz-crm
```

Restart no other service.

Capture new PID and prove process start time is after current `dist/index.js` mtime. If stale, STOP.

Poll port `3002` for up to 90 seconds.

## Runtime asset gate

Check Direct and Public three times:

`/super-admin/bilingual-v138.js?v=superadmin-bilingual-v138`

Require:

- HTTP 200
- JavaScript Content-Type
- Cache-Control no-store
- body contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V138`
- no HTML fallback

## Browser QA

Fresh authenticated browser, cache disabled.

Re-run regressions EN then AR:

1. Users
2. Overview
3. Companies
4. Tenant Details
5. Platform Admins
6. Activity
7. Audit Log

### Audit Log EN — primary V1.38 gate

Open `#audit`.

Require:

- `lang=en`
- `dir=ltr`
- `#auditAction` placeholder exactly `e.g. subscription or github.sync`
- canonical EN severity options remain correct.

Forbidden:

`مثل subscription أو github.sync`

Expected:

`AUDIT LOG EN STATIC UI: NONE FOUND`

### Audit Log AR

Switch to Arabic.

Require `#auditAction` placeholder exactly:

`مثل subscription أو github.sync`

Expected:

`AUDIT LOG AR STATIC UI: NONE FOUND`

If all pass, continue GitHub Sync EN/AR and then Full Audit:

1. Evolution API EN/AR
2. Tara APIs EN/AR
3. Plans Catalog EN/AR
4. Plan Editor EN/AR
5. Company Overrides EN/AR
6. Commercial EN/AR
7. Billing EN/AR
8. Subscriptions EN/AR
9. Settings EN/AR
10. Source Code EN/AR

At the first genuine ordinary untranslated static UI: STOP immediately. Do not fix manually. Capture language, page/hash, exact text, selector/attribute, raw browser finding, and screenshot.

Create:

`TCRMMT_V138_Evidence.zip`

No commit. No push.

## Session handoff

Upload the final report and Evidence ZIP inside the user's ChatGPT Session named exactly:

`TCRMMMT`
