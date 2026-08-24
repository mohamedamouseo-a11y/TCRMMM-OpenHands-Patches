# TCRMMT Super Admin Bilingual V1.31 — GitHub Sync Final Canonicalization

## Scope
Apply only `apply_superadmin_bilingual_v1_31.py` to `/var/www/TCRMMT`.

V1.30 passed apply/build/dist/runtime and all prior regressions through Audit Log, but its GitHub Sync AR closure reintroduced mixed Arabic into GitHub Sync EN. V1.31 adds a **final page-scoped canonicalization pass** inside the existing English/Arabic pattern functions, limited to `#github`, so later generic substitutions cannot re-break GitHub Sync strings.

Do not translate runtime/domain data: URLs, IPs, dates/timestamps, repository/branch names, commit SHAs, event payloads, IDs, role values. `GitHub` and `PAT` remain permitted technical tokens.

## Corrected revision after first V1.31 apply attempt
The first V1.31 evidence stopped before writing because the original patch incorrectly searched from `v122ArabicPatterns` to EOF and saw 16 later `return out;` anchors.

This corrected revision bounds the Arabic target function between:
- start: `const v122ArabicPatterns=(value)=>{`
- end: `const v121PhraseArToEn=`

It still requires exactly one `return out;` inside that bounded function and refuses unknown baselines.

If the previous failed attempt left these **untracked helper files** in `/var/www/TCRMMT` root:
- `VERIFY.md`
- `apply_superadmin_bilingual_v1_31.py`

first confirm they are untracked with `git status --short`, then remove **only those two untracked helper copies**. Do not remove or restore any tracked project file. Run the corrected patch from a temporary directory or directly from the fetched patch-repo working copy; do not copy helper files into the project root again.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_30_GITHUB_SYNC_AR_FULL_PAGE_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_31.py`

Run it twice.

First run must print:
`Applied Super Admin Bilingual V1.31 GitHub Sync final canonicalization runtime.`

Second run must print:
`Super Admin bilingual V1.31 GitHub Sync final canonicalization already applied; no changes made.`

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
`dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_31_GITHUB_SYNC_FINAL_CANONICALIZATION`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V131`
- `/super-admin/bilingual-v131.js`
- `superadmin-bilingual-v131`

## Restart / readiness
Only after all static/build/dist gates pass:
`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v131.js?v=superadmin-bilingual-v131`

Expected: HTTP 200, JavaScript Content-Type, `Cache-Control: no-store`, V131 runtime marker.

## Regression gates
Fresh browser context, cache disabled. Re-run:
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

Required exact/canonical values include:
- `Review platform source and execute sync safely`
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
- `Brief description of changes`
- `Search operation, repository, or user`
- audit category `Other` where applicable
- operation count format `N of N operations`

Explicitly forbid the V1.30 EN regressions:
- `Review Source المنصة وتنفيذ المزامنة بأمان`
- `Review المزامنة وتنفيذها`
- `افحص التغييرات، راجع Files، ثم نفّذ الالتزام والدفع وتحقق من النتيجة.`
- `Connection Status وPAT`
- ordinary static category `أخرى`

Scan visible text, placeholders, `title`, and `aria-label`.

Expected:
`GITHUB SYNC EN STATIC UI: NONE FOUND`

## GitHub Sync AR full gate
Switch to Arabic and verify `lang="ar"`, `dir="rtl"`.

Required canonical values include:
- `مراجعة مصدر المنصة وتنفيذ المزامنة بأمان`
- `● متصل`
- `⟳ تحديث الحالة`
- `مراجعة المزامنة وتنفيذها`
- `افحص التغييرات، راجع الملفات، ثم نفّذ الالتزام والدفع وتحقق من النتيجة.`
- `فحص`
- `تحقق`
- `الإجراء`
- `رسالة الالتزام`
- `ابدأ بمعاينة الفروق لعرض ملخص التغييرات.`
- `ستظهر الملفات هنا بعد المعاينة.`
- `حالة المزامنة`
- `جاهز للتنفيذ`
- `لم تبدأ أي عملية بعد.`
- `التفاصيل التقنية`
- `معلومات المستودع`
- `الصلاحية`
- `حالة الاتصال وPAT`
- `الاتصال`
- `تم حفظ PAT دقيق الصلاحيات`
- `معلومات الفرع والإصدار`
- `نشر معلّق`
- `المصدر متزامن مع GitHub ويوجد إصدار لم يُنشر بعد.`
- `حفظ المستودع والفرع`
- `GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ البناء ثم إعادة التشغيل عند وقت النشر المناسب.`
- `وصف مختصر للتغييرات`
- `بحث في العملية أو المستودع أو المستخدم`
- audit category `أخرى` where applicable
- operation count format `N من N عملية`

Explicitly forbid mixed forms from V1.29/V1.30, including `Source`, `execute`, `Files`, `Commit`, `Push`, `Technical`, `deployment`, `Repository`, `Build`, `Restart` when they occur inside otherwise Arabic static UI. `GitHub` and `PAT` are allowed.

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

Send `TCRMMT_V131_Evidence.zip` and final report. No commit or push.
