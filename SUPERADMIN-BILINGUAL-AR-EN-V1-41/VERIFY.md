# TCRMMT Super Admin Bilingual V1.41 — Evolution API EN Remaining Static Closure

## Scope
Evidence-backed closure for the two remaining ordinary static Arabic strings on `#evolution-api` in English mode.

### Canonical EN ↔ AR
- `Enable Evolution API integration` ↔ `تفعيل تكامل Evolution API`
- `Generate or rotate connection credentials and restart the Evolution API service.` ↔ `توليد أو تدوير بيانات الربط وإعادة تشغيل خدمة Evolution API.`

No runtime/domain data is translated.

## Apply
```bash
cd /var/www/TCRMMT
git status --short
python3 /PATH/TO/SUPERADMIN-BILINGUAL-AR-EN-V1-41/apply_superadmin_bilingual_v1_41.py
python3 /PATH/TO/SUPERADMIN-BILINGUAL-AR-EN-V1-41/apply_superadmin_bilingual_v1_41.py
```

Expected first:
`Applied Super Admin Bilingual V1.41 Evolution API EN remaining static closure runtime.`

Expected second:
`Super Admin bilingual V1.41 Evolution API EN remaining static closure already applied; no changes made.`

Only tracked source allowed modified:
`server/superAdminUiPolish.ts`

## Static gates
```bash
git diff --check
npm run check
npm run build
```
All PASS.

Confirm source/dist:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_41_EVOLUTION_API_EN_REMAINING_STATIC_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V141`
- `/super-admin/bilingual-v141.js`
- `superadmin-bilingual-v141`

## Restart + stale-process guard
After build only:
```bash
pm2 restart tamiyouz-crm
```
Restart only `tamiyouz-crm`.

Prove the new PID process start time is AFTER current `dist/index.js` mtime. If stale: STOP.
Poll port 3002 for readiness, max 90s.

## Runtime asset gate
Test Direct and Public 3 times each:
- `http://127.0.0.1:3002/super-admin/bilingual-v141.js?v=superadmin-bilingual-v141`
- `https://tcrmmm.tamiyouz.com/super-admin/bilingual-v141.js?v=superadmin-bilingual-v141`

Each must be:
- HTTP 200
- JavaScript Content-Type
- no-store
- contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V141`
- never HTML fallback

## Browser QA
Fresh authenticated browser, cache disabled, cache-busted URL.

Rerun regression pages EN/AR:
Users, Overview, Companies, Tenant Details, Platform Admins, Activity, Audit Log, GitHub Sync.

If Tenant Details transient skeleton appears, recheck cleanly up to 3 times before classifying. Do not patch/restart for a transient first attempt.

### Evolution API EN — primary V1.41 gate
Open `#evolution-api`, `lang=en`, `dir=ltr`.

Required ordinary static text includes:
- `Enable Evolution API integration`
- `Generate or rotate connection credentials and restart the Evolution API service.`

Also preserve all eight V1.40 English strings.

Forbidden:
- `تفعيل تكامل Evolution API`
- `توليد أو تدوير بيانات الربط وإعادة تشغيل خدمة Evolution API.`

Expected:
`EVOLUTION API EN STATIC UI: NONE FOUND`

Do not click Save/Test/Refresh/Generate/Rotate or other mutating controls.

### Evolution API AR
Switch to `lang=ar`, `dir=rtl`.

Required:
- `تفعيل تكامل Evolution API`
- `توليد أو تدوير بيانات الربط وإعادة تشغيل خدمة Evolution API.`

Expected:
`EVOLUTION API AR STATIC UI: NONE FOUND`

## Continue Full Audit
If Evolution API EN/AR PASS, continue:
1. Tara APIs EN/AR
2. Plans Catalog EN/AR
3. Plan Editor EN/AR
4. Company Overrides EN/AR
5. Commercial EN/AR
6. Billing EN/AR
7. Subscriptions EN/AR
8. Settings EN/AR
9. Source Code EN/AR

At first genuine ordinary untranslated static UI: STOP. No manual fix. Capture language, page/hash, exact text, untranslated segment, selector/attribute, raw browser finding, screenshot.

Exclude runtime/domain data: names, company names, emails, dates/timestamps, IDs, paths, tenant/product/plan values, roles, URLs, IPs, repo/branch/SHA, event payloads, raw technical errors.

## Evidence
Create `TCRMMT_V141_Evidence.zip`.

No commit. No push.

Upload the final report and Evidence ZIP inside ChatGPT Session exactly:
`TCRMMMT`
