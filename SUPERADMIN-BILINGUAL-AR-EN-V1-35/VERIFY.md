# TCRMMT Super Admin Bilingual V1.35 — GitHub Sync EN Remaining Static Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_35.py` to `/var/www/TCRMMT`.

Evidence basis: V1.34 passed apply/check/build/runtime asset and all browser regressions through Audit Log EN/AR. The V1.34 GitHub Sync EN raw browser scan then showed three confirmed ordinary static UI leaks on `#github`: the mixed subtitle `Review مصدر المنصة وتنفيذ المزامنة بأمان`, the filter option `كل العمليات`, and action text `إلغاء آمن`.

Do not translate runtime/domain data such as event names/payloads, names, emails, paths, dates/timestamps, IDs, URLs, IPs, repository/branch/SHA values, PAT, or role/runtime values.

## Safety
No manual source edits, reset/clean/restore, DB/migration/Nginx changes, unrelated PM2 restarts, commit, or push.
Only `server/superAdminUiPolish.ts` may change.

## Apply
Run official patch twice.
First run exact output:
`Applied Super Admin Bilingual V1.35 GitHub Sync EN remaining static closure runtime.`
Second run exact output:
`Super Admin bilingual V1.35 GitHub Sync EN remaining static closure already applied; no changes made.`

## Static gates
Run `git diff --check`, `npm run check`, `npm run build`. All PASS.
Verify dist contains:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_35_GITHUB_SYNC_EN_REMAINING_STATIC_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V135`
- `/super-admin/bilingual-v135.js`
- `superadmin-bilingual-v135`

## Restart / stale guard
Restart only `tamiyouz-crm` after gates pass. Capture new PID and prove process start time is after current `dist/index.js` mtime. If stale, STOP.
Poll port 3002 up to 90 seconds.

## Runtime asset
Direct and Public `/super-admin/bilingual-v135.js?v=superadmin-bilingual-v135`, 3 times each. Require HTTP 200, JavaScript Content-Type, no-store, V135 marker. HTML fallback = STOP.

## Browser regressions
Fresh browser + cache disabled. Re-run EN/AR:
Users, Overview, Companies, Tenant Details, Platform Admins, Activity, Audit Log.

## GitHub Sync EN primary gate
On `#github`, `lang=en`, `dir=ltr`, require at least:
- `GitHub Advanced Sync`
- `Review platform source and execute sync safely`
- `All operations`
- `Safe cancel`
- `Preview Diff`
- `Review & Sync`
- `Refresh Log`

Forbid ordinary static leaks:
- `Review مصدر المنصة وتنفيذ المزامنة بأمان`
- `كل العمليات`
- `إلغاء آمن`

Do not flag GitHub audit/event payload text such as `github.preview`, `github.operation_failed`, URLs, IPs, timestamps, `Super Admin`, repository data, or event metadata.
Expected: `GITHUB SYNC EN STATIC UI: NONE FOUND`.

## GitHub Sync AR
Switch to Arabic. Require canonical Arabic for the same ordinary static UI:
- `مزامنة GitHub المتقدمة`
- `مراجعة مصدر المنصة وتنفيذ المزامنة بأمان`
- `كل العمليات`
- `إلغاء آمن`

Expected: `GITHUB SYNC AR STATIC UI: NONE FOUND`.

## Continue full audit
If GitHub Sync EN/AR PASS, continue:
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

At first genuine ordinary untranslated static UI: STOP immediately, do not fix manually. Record language, page/hash, exact text, untranslated segment, selector/attribute, raw browser finding, screenshot.

Create `TCRMMT_V135_Evidence.zip`.
No commit. No push.

## Session handoff
Put/upload final report and Evidence ZIP inside the user's ChatGPT Session named exactly:
`TCRMMMT`
