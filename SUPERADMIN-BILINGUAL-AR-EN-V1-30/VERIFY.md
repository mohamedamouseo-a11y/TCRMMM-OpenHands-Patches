# TCRMMT Super Admin Bilingual V1.30 — GitHub Sync AR Full-Page Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_30.py` to `/var/www/TCRMMT`.

V1.29 passed static/build/runtime and the full GitHub Sync EN gate. The V1.29 Full Audit then stopped in GitHub Sync AR after a page-wide scan exposed a set of ordinary mixed/static Arabic UI strings.

V1.30 closes the complete evidenced mixed/static set in GitHub Sync AR in one atomic patch. `GitHub` and `PAT` remain permitted product/technical tokens. Runtime/domain data (URLs, IPs, dates/timestamps, repository/branch values, commit SHAs, event payloads, IDs, role values) must remain untouched.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_29_GITHUB_SYNC_EN_FULL_PAGE_CLOSURE`

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_30.py`

Run it twice.

First run must print:
`Applied Super Admin Bilingual V1.30 GitHub Sync AR full-page closure runtime.`

Second run must print:
`Super Admin bilingual V1.30 GitHub Sync AR full-page closure already applied; no changes made.`

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
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_30_GITHUB_SYNC_AR_FULL_PAGE_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V130`
- `/super-admin/bilingual-v130.js`
- `superadmin-bilingual-v130`

## Restart / readiness
Only after all static/build/dist gates pass:
`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds.

## Runtime gates
Verify Direct and Public:
- `/super-admin`
- `/super-admin/bilingual-v130.js?v=superadmin-bilingual-v130`

Expected: HTTP 200, JavaScript Content-Type, `Cache-Control: no-store`, runtime V130 marker.

## Regression gates
Use a fresh browser context with cache disabled. Re-run:
- Users EN / AR
- Overview EN / AR
- Companies EN / AR
- Tenant Details EN / AR
- Platform Admins EN / AR
- Activity EN / AR
- Audit Log EN / AR
- GitHub Sync EN

Any regression = STOP.

## GitHub Sync AR full gate
Open `#github` in Arabic and verify `lang="ar"`, `dir="rtl"`.

The following ordinary static values must be fully Arabic:
- `مراجعة مصدر المنصة وتنفيذ المزامنة بأمان`
- `مراجعة المزامنة وتنفيذها`
- `افحص التغييرات، راجع الملفات، ثم نفّذ الالتزام والدفع وتحقق من النتيجة.`
- `رسالة الالتزام`
- `ابدأ بمعاينة الفروق لعرض ملخص التغييرات.`
- `ستظهر الملفات هنا بعد المعاينة.`
- `التفاصيل التقنية`
- `حالة الاتصال وPAT`
- `تم حفظ PAT دقيق الصلاحيات`
- `نشر معلّق`
- `حفظ المستودع والفرع`
- `GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ البناء ثم إعادة التشغيل عند وقت النشر المناسب.`

Explicitly forbid the V1.29 mixed forms:
- `مراجعة Source المنصة وتنفيذ المزامنة بأمان`
- `مراجعة & execute sync`
- `افحص التغييرات، راجع Files، ثم نفّذ Commit وPush وتحقق من النتيجة.`
- `رسالة Commit`
- `Start with معاينة الفروق to display a summary of changes.`
- `ابدأ بPreview Diff لعرض ملخص التغييرات.`
- `ستظهر Files هنا بعد المعاينة.`
- `Technical تفاصيل`
- `الDetails التقنية`
- `حالة الاتصال & PAT`
- `Connection Status و PAT`
- `Fine-grained PAT محفوظ`
- `معلقة deployment`
- `حفظ Repository والفرع`
- `GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ Build ثم Restart عند وقت النشر المناسب.`

Scan visible text, placeholders, `title`, and `aria-label`.

Allowed/excluded from untranslated-static classification: `GitHub`, `PAT`, `Tara API`, runtime/data values including repository/branch names, URLs, IPs, dates/timestamps, commit SHAs, event payloads, IDs and role values.

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

Send `TCRMMT_V130_Evidence.zip` and final report. No commit or push.
