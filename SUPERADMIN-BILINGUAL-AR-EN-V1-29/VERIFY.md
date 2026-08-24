# TCRMMT Super Admin Bilingual V1.29 — GitHub Sync EN Full-Page Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_29.py` to `/var/www/TCRMMT`.

V1.28 passed apply/build/runtime, all prior regressions, Activity EN/AR, and Audit Log EN/AR. Full Audit then stopped at GitHub Sync EN.

V1.29 closes the complete ordinary static Arabic/mixed set exposed by the V1.28 GitHub Sync EN raw scan, including connection status/action text, sync review headings/labels/empty states/progress text, repository/PAT/branch/deployment labels and messages, save action, commit/search placeholders, and the dynamic audit-count UI pattern (`N من M عملية` -> `N of M operations`).

Do not translate runtime/domain data such as URLs, IP addresses, dates/timestamps, role values, repository names, commit SHAs, audit payload values, account/person/company names, plan/product values, or IDs.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_28_ACTIVITY_EN_VIEW_ALL_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_29.py`

Run it twice.

First run must print:
`Applied Super Admin Bilingual V1.29 GitHub Sync EN full-page closure runtime.`

Second run must be no-op:
`Super Admin bilingual V1.29 GitHub Sync EN full-page closure already applied; no changes made.`

## Safety
No manual source edits, reset, clean, restore, commit, push, DB/migration changes, Nginx changes, or unrelated PM2 changes.

## Static gates
Only `server/superAdminUiPolish.ts` may change.

Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

## Dist gate
Before restart, `dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_29_GITHUB_SYNC_EN_FULL_PAGE_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V129`
- `/super-admin/bilingual-v129.js`
- `superadmin-bilingual-v129`

## Restart / readiness
Only after all static/build/dist gates pass:
`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v129.js?v=superadmin-bilingual-v129`

Expected:
- HTTP 200
- JavaScript Content-Type for the runtime asset
- `Cache-Control: no-store`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V129`

## Regression gates
Fresh browser context, cache disabled.

Re-run:
- Users EN / AR
- Overview EN / AR
- Companies EN / AR
- Tenant Details EN / AR
- Platform Admins EN / AR
- Activity EN / AR
- Audit Log EN / AR

Any regression = STOP.

## GitHub Sync EN full gate
Open `#github` in English and verify `lang="en"`, `dir="ltr"`.

Required canonical values include:
- `● Connected`
- `⟳ Refresh status`
- `Review & execute sync`
- `Inspect changes, review Files, then run Commit and Push and verify the result.`
- `Check`
- `Verify`
- `Action`
- `Commit message`
- `Start with Preview Diff to display a summary of changes.`
- `Files will appear here after preview.`
- `Sync status`
- `Ready to execute`
- `No operation has started yet.`
- `Ready to execute.`
- `Technical Details`
- `Repository information`
- `Permission`
- `Connection Status & PAT`
- `Connection`
- `Fine-grained PAT saved`
- `Branch and release information`
- `Pending deployment`
- `Source is synced with GitHub and there is an undeployed release.`
- `Save Repository and branch`
- `GitHub is ready. There is an unbuilt release; run Build then Restart at the appropriate deployment time.`
- placeholder `Brief description of changes`
- placeholder `Search operation, repository, or user`
- audit count pattern `<N> of <M> operations`

Explicitly forbid the V1.28 raw static Arabic/mixed forms:
- `● متصل`
- `⟳ تحديث الحالة`
- `Review وتنفيذ المزامنة`
- `افحص التغييرات، راجع Files، ثم نفّذ Commit وPush وتحقق من النتيجة.`
- `فحص`
- `تحقق`
- `الإجراء`
- `رسالة Commit`
- `ابدأ بPreview Diff لعرض ملخص التغييرات.`
- `ستظهر Files هنا بعد المعاينة.`
- `حالة المزامنة`
- `جاهز للتنفيذ`
- `لم تبدأ أي عملية بعد.`
- `جاهز للتنفيذ.`
- `الDetails التقنية`
- `معلومات المستودع`
- `الصلاحية`
- `Connection Status و PAT`
- `الاتصال`
- `Fine-grained PAT محفوظ`
- `معلومات الفرع والإصدار`
- `ينتظر النشر`
- `المصدر متزامن مع GitHub ويوجد إصدار لم يُنشر بعد.`
- `حفظ Repository والفرع`
- `GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ Build ثم Restart عند وقت النشر المناسب.`
- placeholder `وصف مختصر للتغييرات`
- placeholder `بحث في العملية أو المستودع أو المستخدم`
- count pattern `<N> من <M> عملية`

Scan visible text, placeholders, `title`, and `aria-label`. Exclude only runtime/domain data listed in Scope.

Expected:
`GITHUB SYNC EN STATIC UI: NONE FOUND`

## GitHub Sync AR gate
Switch to Arabic and verify `lang="ar"`, `dir="rtl"`.

Verify the corresponding Arabic canonical strings, including the connection badge/action, review/progress labels, repository/PAT/branch/deployment text, Arabic placeholders, and audit count pattern `<N> من <M> عملية`.

Expected:
`GITHUB SYNC AR STATIC UI: NONE FOUND`

## Continue remaining Full Audit
Only if GitHub Sync EN and AR both PASS, continue EN + AR:
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

Send `TCRMMT_V129_Evidence.zip` and final report. No commit or push.
