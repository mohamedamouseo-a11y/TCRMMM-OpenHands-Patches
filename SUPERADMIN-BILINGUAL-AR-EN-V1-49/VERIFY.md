# TCRMMT Super Admin Bilingual V1.49 — Plans Runtime Status / Empty-State Closure

## Scope

Target: `/var/www/TCRMMT`

Official patch:
- `apply_superadmin_bilingual_v1_49.py`

Expected cumulative tracked production scope remains:
- `server/superAdminUiPolish.ts`
- `server/_core/index.ts`

V1.49 itself may modify only `server/superAdminUiPolish.ts`.

Do not manually edit, reset, clean, restore, commit, or push.

## Preflight

```bash
cd /var/www/TCRMMT
git status --short
grep -c 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_48_PLANS_CATALOG_EDITOR_FULL_STATIC_CLOSURE' server/superAdminUiPolish.ts
grep -c 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_49_PLANS_RUNTIME_STATUS_EMPTY_STATE_CLOSURE' server/superAdminUiPolish.ts
```

V1.48 prerequisite must exist. V1.49 must be absent before first apply.

## Apply twice

```bash
python3 apply_superadmin_bilingual_v1_49.py
python3 apply_superadmin_bilingual_v1_49.py
```

Expected first:
`Applied Super Admin Bilingual V1.49 Plans runtime status/empty-state closure.`

Expected second:
`Super Admin bilingual V1.49 Plans runtime status/empty-state closure already applied; no changes made.`

## Static gates

```bash
git status --short
git diff --check
npm run check
npm run build
```

All must pass. Confirm `dist/index.js` contains:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_49_PLANS_RUNTIME_STATUS_EMPTY_STATE_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V149`
- `/super-admin/bilingual-v149.js`
- `superadmin-bilingual-v149`

## Restart / stale guard

Restart only:
```bash
pm2 restart tamiyouz-crm
```

Prove the new PM2 process start time is strictly later than current `dist/index.js` mtime. If stale, STOP.

Poll port 3002 for readiness for at most 90 seconds.

## Runtime asset

Check Direct and Public three times each:

- `http://127.0.0.1:3002/super-admin/bilingual-v149.js?v=superadmin-bilingual-v149`
- `https://tcrmmm.tamiyouz.com/super-admin/bilingual-v149.js?v=superadmin-bilingual-v149`

Each response must be:
- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V149`
- not HTML fallback

## Regressions

Fresh authenticated browser, cache disabled.

Read-only only. Do not activate mutating actions or read secret values.

Recheck:
1. V1.46 direct `#evolution-api` + hash away/back
2. Evolution API EN/AR
3. Tara APIs EN/AR
4. Tara Add Integration modal open/close only

Expected:
- `EVOLUTION API EN STATIC UI: NONE FOUND`
- `EVOLUTION API AR STATIC UI: NONE FOUND`
- `TARA APIs EN STATIC UI: NONE FOUND`
- `TARA APIs AR STATIC UI: NONE FOUND`

## Plans Catalog EN — primary V1.49 gate

Open a fresh cache-busted `/super-admin/plans` session and switch using the normal language control to:
- `lang=en`
- `dir=ltr`
- Plans tab active

Do not Save, Clone, Publish, Assign, or perform any mutation.

V1.48 evidence blocker:

`#status` must NOT contain:
`جاهز — جميع مفاتيح التشغيل تبدأ بأمان ويمكن تفعيلها تدريجيًا`

It must be exactly:
`Ready — all operational controls start safely and can be enabled progressively.`

Also verify the Plans empty editor state, if visible, is exactly:
`Select a plan to view its details`

Forbidden mixed/static variants include:
- `اختر باقة لعرض تفاصيلها`
- `اختر باقة لعرض Detailsها`

Then complete the full V1.48 Plans Catalog EN gate. Expected:
`PLANS CATALOG EN STATIC UI: NONE FOUND`

## Plan Editor EN

Open an existing plan read-only. Do not modify/save/publish/clone.

Complete the V1.48 Plan Editor gate, including dynamic status/count/helper text.

Expected:
`PLAN EDITOR EN STATIC UI: NONE FOUND`

## Plans Catalog + Plan Editor AR

Use the normal language control:
- `lang=ar`
- `dir=rtl`

Required status:
`جاهز — جميع مفاتيح التشغيل تبدأ بأمان ويمكن تفعيلها تدريجيًا`

Required empty editor state, if visible:
`اختر باقة لعرض تفاصيلها`

Complete all V1.48 Arabic checks.

Expected:
- `PLANS CATALOG AR STATIC UI: NONE FOUND`
- `PLAN EDITOR AR STATIC UI: NONE FOUND`

Plan names, slugs, versions, counts, company names, feature/product/catalog values, and other runtime/domain values are not static translation blockers.

## Continue Full Audit

If V1.49 primary + reverse gates pass, continue EN then AR:
1. Company Overrides
2. Commercial
3. Billing
4. Subscriptions
5. Settings
6. Source Code

At the FIRST genuine ordinary untranslated static UI:
STOP immediately.

Do not fix it manually. Capture:
- language
- page/hash/tab
- exact text
- untranslated segment
- selector/attribute
- raw browser finding
- screenshot

Exclude runtime/domain data such as names, emails, IDs, counts, plan/product values, dates/timestamps, paths, URLs, IPs, roles, repo/branch/SHA, masked secrets, event payloads, and raw technical errors.

## Evidence

Create:
`TCRMMT_V149_Evidence.zip`

Include:
- preflight
- apply/no-op
- tracked scope
- static gates
- source/dist/runtime markers
- restart/stale proof
- Direct/Public runtime asset 3x
- regressions
- V1.49 Plans EN status + empty-state evidence
- Plans Catalog EN / Plan Editor EN
- Plans Catalog AR / Plan Editor AR
- Full Audit progress
- first genuine blocker if found
- screenshots
- final report

No commit. No push.

Upload the final report and `TCRMMT_V149_Evidence.zip` inside ChatGPT Session exactly named `TCRMMMT`.
