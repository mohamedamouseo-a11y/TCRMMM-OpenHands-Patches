# TCRMMT Super Admin Bilingual V1.32 — GitHub Sync AR Remaining Static Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_32.py` to `/var/www/TCRMMT`.

Corrected V1.31 passed apply/build/dist/runtime, all previous EN/AR regressions through Audit Log, and the full GitHub Sync EN gate. GitHub Sync AR then stopped at the first genuine mixed subtitle. The same V1.31 evidence/raw selector scan also proved a small remaining ordinary-static set on `#github`:

- `GitHub Advanced Sync` → `مزامنة GitHub المتقدمة`
- `مراجعة platform source and execute sync safely` → `مراجعة مصدر المنصة وتنفيذ المزامنة بأمان`
- `Commit` → `الالتزام`
- `Push` → `الدفع`
- `Token` → `رمز الوصول`
- `Deployment` → `النشر`

V1.32 adds a final page-scoped canonicalization pass limited to `#github`. Do not translate runtime/domain data such as repository/branch names, URLs, IPs, dates/timestamps, commit SHAs, IDs, audit event names/payloads, role values, or other runtime values. `GitHub` and `PAT` remain permitted technical tokens.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_31_GITHUB_SYNC_FINAL_CANONICALIZATION`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_32.py`

Run twice.

First run must print:
`Applied Super Admin Bilingual V1.32 GitHub Sync AR remaining static closure runtime.`

Second run must print:
`Super Admin bilingual V1.32 GitHub Sync AR remaining static closure already applied; no changes made.`

## Safety
No manual source edits, reset, clean, restore, commit, push, DB/migration changes, Nginx changes, or unrelated PM2 changes.

## Static gates
Only `server/superAdminUiPolish.ts` may be tracked-modified.

Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

## Dist gate
`dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_32_GITHUB_SYNC_AR_REMAINING_STATIC_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V132`
- `/super-admin/bilingual-v132.js`
- `superadmin-bilingual-v132`

## Restart/readiness
Only after all gates pass:
`pm2 restart tamiyouz-crm`

Readiness poll port `3002` for up to 90 seconds.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v132.js?v=superadmin-bilingual-v132`

Expected: HTTP 200, JavaScript Content-Type, `Cache-Control: no-store`, V132 runtime marker.

## Regression gates
Fresh browser context with cache disabled. Re-run:
- Users EN / AR
- Overview EN / AR
- Companies EN / AR
- Tenant Details EN / AR
- Platform Admins EN / AR
- Activity EN / AR
- Audit Log EN / AR

Any regression = STOP.

## GitHub Sync EN
Open `#github` in EN and verify `lang="en"`, `dir="ltr"`.

The full V1.31 English canonical gate must remain PASS, including:
- `GitHub Advanced Sync`
- `Review platform source and execute sync safely`
- `Review & execute sync`
- `Inspect changes, review Files, then run Commit and Push and verify the result.`
- `Commit`
- `Push`
- `Token`
- `Deployment`
- `Connection Status & PAT`
- operation count `N of N operations`

Expected:
`GITHUB SYNC EN STATIC UI: NONE FOUND`

## GitHub Sync AR full gate
Switch to AR and verify `lang="ar"`, `dir="rtl"`.

Required canonical static values include all prior V1.31 Arabic values plus:
- `مزامنة GitHub المتقدمة`
- `مراجعة مصدر المنصة وتنفيذ المزامنة بأمان`
- `الالتزام`
- `الدفع`
- `رمز الوصول`
- `النشر`

Explicitly forbid ordinary-static remnants:
- `GitHub Advanced Sync`
- `مراجعة platform source and execute sync safely`
- standalone static `Commit`
- standalone static `Push`
- standalone static `Token`
- standalone static `Deployment`

`GitHub`, `PAT`, repository/branch names, SHA, audit event names such as `github.sync`, URLs, IPs, timestamps, IDs, role/runtime values remain allowed data/technical tokens.

Scan visible text, placeholders, `title`, and `aria-label`.

Expected:
`GITHUB SYNC AR STATIC UI: NONE FOUND`

## Continue remaining Full Audit
Only if GitHub Sync EN and AR both PASS, continue EN + AR in order:
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

On the first genuine ordinary untranslated static UI: **STOP immediately. Do not fix manually.**

Record language, page/hash, exact text, untranslated segment, selector/attribute, raw browser finding, and screenshot.

Send `TCRMMT_V132_Evidence.zip` plus final report. No commit or push.
