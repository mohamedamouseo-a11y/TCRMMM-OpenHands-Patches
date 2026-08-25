# TCRMMT Super Admin Bilingual V1.40 — VERIFY

## Scope
Evidence-backed closure for Evolution API EN ordinary static UI only.

Target:
`/var/www/TCRMMT/server/superAdminUiPolish.ts`

Required previous marker:
`SUPER_ADMIN_BILINGUAL_AR_EN_V1_39_GITHUB_SYNC_AR_SAFE_CLEANUP_OPTION_CLOSURE`

New marker:
`SUPER_ADMIN_BILINGUAL_AR_EN_V1_40_EVOLUTION_API_EN_STATIC_CLOSURE`

Runtime:
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V140`
- `/super-admin/bilingual-v140.js`
- `superadmin-bilingual-v140`

## Apply
Run the official patch twice.

Expected first:
`Applied Super Admin Bilingual V1.40 Evolution API EN static closure runtime.`

Expected second:
`Super Admin bilingual V1.40 Evolution API EN static closure already applied; no changes made.`

No manual edits.

## Static gates
- `git status --short`
- only tracked modified source may be `server/superAdminUiPolish.ts`
- `git diff --check`
- `npm run check`
- `npm run build`

All PASS.

Confirm source/dist markers and V140 runtime path/cache key.

## Restart
Restart only:
`pm2 restart tamiyouz-crm`

Stale-process guard is mandatory:
new PID process start time must be after current `dist/index.js` mtime.
If stale, STOP.

Readiness: port 3002 within 90 seconds.

## Runtime asset
Direct/Public V140 runtime asset 3 times each:
- HTTP 200
- JavaScript Content-Type
- no-store
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V140`
- no HTML fallback

## Browser
Fresh authenticated browser, cache disabled.

Re-run regressions EN/AR:
Users, Overview, Companies, Tenant Details, Platform Admins, Activity, Audit Log, GitHub Sync.

### Evolution API EN — primary V1.40 gate
Open `#evolution-api`, `lang=en`, `dir=ltr`.

The following ordinary static UI must be English:

1. `One central setup used by platform companies. Available only to the platform owner, and secrets are not shown after saving.`
2. `Disabling it prevents connections and sending across the platform.`
3. `Loading settings...`
4. `Automatic setup`
5. `Checking automatic management capability...`
6. `Refresh status`
7. `Generate and connect credentials`
8. `Rotate credentials`

Forbidden Arabic static strings:
- `إعداد مركزي واحد تستخدمه شركات المنصة. متاح لمالك المنصة فقط ولا تُعرض الأسرار بعد حفظها.`
- `إيقافه يمنع الاتصال والإرسال على مستوى المنصة.`
- `جاري تحميل الإعدادات...`
- `الإعداد التلقائي`
- `جاري فحص إمكانية الإدارة التلقائية...`
- `تحديث الحالة`
- `توليد وربط البيانات`
- `تدوير البيانات`

Expected:
`EVOLUTION API EN STATIC UI: NONE FOUND`

### Evolution API AR
Switch to `lang=ar`, `dir=rtl`.

The same 8 strings must canonicalize back to the Arabic forms above.

Expected:
`EVOLUTION API AR STATIC UI: NONE FOUND`

Do not activate Generate, Rotate, Save, Test, Refresh, or any mutating Evolution API action.

## Continue Full Audit
Only if Evolution API EN/AR PASS:
1. Tara APIs EN/AR
2. Plans Catalog EN/AR
3. Plan Editor EN/AR
4. Company Overrides EN/AR
5. Commercial EN/AR
6. Billing EN/AR
7. Subscriptions EN/AR
8. Settings EN/AR
9. Source Code EN/AR

At first genuine ordinary untranslated static UI:
STOP. No manual fix. Capture language, page/hash, exact text, selector/attribute, raw browser finding, screenshot.

Exclude runtime/domain data: names, emails, IDs, paths, tenant/product/plan values, roles, timestamps, URLs, IPs, repo/branch/SHA, event payloads, raw technical errors.

## Evidence
Create `TCRMMT_V140_Evidence.zip`.

No commit. No push.

Upload final report + evidence ZIP to ChatGPT Session exactly:
`TCRMMMT`
