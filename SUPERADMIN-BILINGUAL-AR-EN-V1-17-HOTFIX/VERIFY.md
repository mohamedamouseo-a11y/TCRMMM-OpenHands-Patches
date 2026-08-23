# TCRMMT Super Admin Bilingual V1.17 — Startup Hotfix VERIFY

## Scope
Fix only the malformed literal `\\n` inserted by the original V1.17 UI version replacement. Do not change translation semantics or bump the V117 runtime version.

## Hard rules
- Target: `/var/www/TCRMMT`
- Allowed modified file: `server/superAdminUiPolish.ts` only
- No manual edits
- No reset / clean / restore
- No commit / push
- Do not touch Nginx or databases
- Do not rebuild or restart before the hotfix is applied

## Precondition
Source must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE`
- malformed sequence where the V1.17 marker is followed by literal `\\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V117";`

## Apply
Run `apply_superadmin_bilingual_v1_17_startup_hotfix.py` twice.

First run expected:
`Applied Super Admin bilingual V1.17 startup hotfix.`

Second run expected:
`Super Admin bilingual V1.17 startup hotfix already applied; no changes made.`

## Static gates
- `git status --short`
- only `server/superAdminUiPolish.ts` changed
- `git diff --check`
- `npm run check`
- `npm run build`

## Dist startup gate
Confirm `dist/index.js` contains all of:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_STARTUP_HOTFIX`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V117`
- `/super-admin/bilingual-v117.js`

Confirm the compiled startup area no longer evaluates `SUPER_ADMIN_UI_POLISH_VERSION = UI_VERSION` before a definition of `UI_VERSION`.

## Isolated probe BEFORE PM2 restart
Use a free temporary port, default 3102:

```bash
NODE_ENV=production PORT=3102 PROCESS_ROLE=web node dist/index.js \
  > /tmp/tcrmmt_v117_hotfix_probe_stdout.log \
  2> /tmp/tcrmmt_v117_hotfix_probe_stderr.log &
PROBE_PID=$!
sleep 8
ss -ltnp | grep ':3102'
curl -sS -D /tmp/tcrmmt_v117_hotfix_probe_headers.txt \
  -o /tmp/tcrmmt_v117_hotfix_probe.html \
  http://127.0.0.1:3102/super-admin
curl -sS -D /tmp/tcrmmt_v117_hotfix_asset_headers.txt \
  -o /tmp/tcrmmt_v117_hotfix_asset.js \
  'http://127.0.0.1:3102/super-admin/bilingual-v117.js?v=superadmin-bilingual-v117'
kill "$PROBE_PID" 2>/dev/null || true
wait "$PROBE_PID" 2>/dev/null || true
```

Required:
- probe listener exists
- `/super-admin` returns HTTP response
- V117 asset returns HTTP 200
- asset contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V117`
- no `ReferenceError: UI_VERSION is not defined`

If isolated probe fails: STOP. Do not restart PM2.

## Production recovery
Only after isolated probe PASS:
- `pm2 restart tamiyouz-crm`
- confirm service online
- confirm listener on 3002
- direct `/super-admin` responds
- public `/super-admin` is not 502
- public V117 asset is HTTP 200 and contains V117 marker

If stable, run `pm2 save`.

## Resume V1.17 browser QA
Fresh context, cache disabled.

Required regression gates:
- Overview EN/AR: PASS
- Companies EN/AR: PASS
- Tenant Details EN/AR: PASS
- Users EN: `NONE FOUND`
- Users AR: `NONE FOUND`

If Users passes, continue full EN+AR audit from:
1. Platform Admins
2. Activity
3. Audit Log
4. GitHub Sync
5. Evolution API
6. Tara APIs
7. Plans Catalog
8. Plan Editor
9. Company Overrides
10. Commercial
11. Billing
12. Subscriptions
13. Settings
14. Source Code

Stop on first ordinary untranslated static UI. Record exact text, language, page, selector/attribute, and screenshot. Do not fix manually.
