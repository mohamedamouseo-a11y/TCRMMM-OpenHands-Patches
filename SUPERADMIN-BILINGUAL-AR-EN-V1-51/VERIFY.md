# TCRMMT Super Admin Bilingual V1.51 — VERIFY

## Purpose

V1.50 evidence proved V1.50 itself PASS and Tara EN/AR PASS. The next blocker is Plans language persistence:

- Main Super Admin is EN.
- Normal Plans navigation hard-navigates with `location.assign('/super-admin/plans')`.
- Standalone Plans HTML is emitted as `<html lang="ar" dir="rtl">`.
- Plans finishes AR/RTL, so V1.49 status/empty-state EN closure never becomes active.

V1.51 makes the hard-navigation language handoff explicit:

1. Main Plans navigation sends `?lang=ar|en` from current `data-sa-lang`, falling back to `tcrm-super-admin-language`.
2. `/super-admin/plans` bilingual boot treats a valid query `lang` as authoritative before its first sweep and persists it through the existing boot write path.
3. No plan/domain data or Plans API/business logic changes.

## Official patch

Repository: `mohamedamouseo-a11y/TCRMMM-OpenHands-Patches`

Branch: `superadmin-bilingual-ar-en-v1-51`

Folder: `SUPERADMIN-BILINGUAL-AR-EN-V1-51`

Files:
- `apply_superadmin_bilingual_v1_51.py`
- `VERIFY.md`

Target: `/var/www/TCRMMT`

Production branch stays `master`. No new production branch. No PR.

## Allowed cumulative tracked modified scope

Only:
- `server/superAdminUiPolish.ts`
- `server/_core/index.ts`

V1.51 intentionally touches both. Any other tracked modification: STOP. Do not reset/clean/restore.

## Preflight

```bash
cd /var/www/TCRMMT
git status --short
git branch --show-current
git rev-parse HEAD
```

Must be `master`.

Confirm V1.50 marker in `server/superAdminUiPolish.ts`:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1_50_TARA_LANGUAGE_ATTRIBUTE_RESWEEP`

Confirm V1.46 functional marker in `server/_core/index.ts`:

`SUPER_ADMIN_EVOLUTION_DIRECT_HASH_RESTORE_V146`

V1.51 marker must be absent from both targets before first apply:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1_51_PLANS_LANGUAGE_NAV_PERSISTENCE`

## Apply twice

Run official V1.51 script twice.

First expected exactly:

`Applied Super Admin Bilingual V1.51 Plans language navigation persistence.`

Second expected exactly:

`Super Admin bilingual V1.51 Plans language navigation persistence already applied; no changes made.`

No manual edits.

## Static gates

Run:

```bash
git diff --check
npm run check
npm run build
```

All PASS.

Confirm source/dist:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_51_PLANS_LANGUAGE_NAV_PERSISTENCE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V151`
- `/super-admin/bilingual-v151.js`
- `superadmin-bilingual-v151`
- Plans boot contains `URLSearchParams` + pathname `/super-admin/plans` + query key `lang`
- built main navigation contains `/super-admin/plans?lang=` and `tcrm-super-admin-language`

## Restart

Restart only:

```bash
pm2 restart tamiyouz-crm
```

Capture `dist/index.js` mtime first. New PM2 start epoch must be strictly greater than dist mtime. If stale: STOP.

Port 3002 readiness <=90 sec.

## Runtime asset

Direct 3x:

`http://127.0.0.1:3002/super-admin/bilingual-v151.js?v=superadmin-bilingual-v151`

Public 3x:

`https://tcrmmm.tamiyouz.com/super-admin/bilingual-v151.js?v=superadmin-bilingual-v151`

Every attempt:
- HTTP 200
- JavaScript content type
- Cache-Control no-store
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V151`
- no HTML fallback

## Evolution regression

Fresh authenticated browser, cache disabled, read-only.

Verify direct `#evolution-api`, hash away/back, one additional loader cycle only, EN canonical and AR canonical.

Expected:
- `EVOLUTION API EN STATIC UI: NONE FOUND`
- `EVOLUTION API AR STATIC UI: NONE FOUND`

No Evolution mutation.

## Tara regression

Repeat V1.50 sequence: AR main → Tara AR → back → natural EN → Tara EN without refresh. Modal open/close read-only only.

Expected:
- `TARA APIs EN STATIC UI: NONE FOUND`
- `TARA APIs AR STATIC UI: NONE FOUND`

No Save/Test/Disable/Delete.

## PRIMARY — Plans EN language handoff

On Main Super Admin select EN using the normal visible language control.

Before clicking Plans prove:

```js
document.documentElement.lang === 'en'
document.documentElement.dir === 'ltr'
document.documentElement.dataset.saLang === 'en'
localStorage.getItem('tcrm-super-admin-language') === 'en'
```

Then click the normal Plans navigation control. Do not manually type the Plans URL for this primary gate.

Final URL must contain:

`/super-admin/plans?lang=en`

Final Plans state:
- `lang=en`
- `dir=ltr`
- `data-sa-lang=en`
- stored language `en`
- Plans tab active

`#status` exactly:

`Ready — all operational controls start safely and can be enabled progressively.`

If empty editor visible:

`Select a plan to view its details`

Forbidden:
- Arabic status
- `اختر باقة لعرض تفاصيلها`
- `اختر باقة لعرض Detailsها`

Complete Plans Catalog EN audit.

Expected:

`PLANS CATALOG EN STATIC UI: NONE FOUND`

## Plan Editor EN

Select one existing plan read-only. Do not Clone/Save/Publish and do not persist fields.

Expected:

`PLAN EDITOR EN STATIC UI: NONE FOUND`

## PRIMARY — Plans AR handoff

Return normally to Main Super Admin. Use normal language control to select AR.

Before Plans prove `lang=ar`, `dir=rtl`, `data-sa-lang=ar`, stored language `ar`.

Click normal Plans navigation.

Final URL must contain:

`/super-admin/plans?lang=ar`

Final Plans state must remain AR/RTL with stored language AR.

`#status` exactly:

`جاهز — جميع مفاتيح التشغيل تبدأ بأمان ويمكن تفعيلها تدريجيًا`

Empty editor if visible:

`اختر باقة لعرض تفاصيلها`

Expected:
- `PLANS CATALOG AR STATIC UI: NONE FOUND`
- `PLAN EDITOR AR STATIC UI: NONE FOUND`

## Query precedence proof

Read-only direct checks:

1. With stored AR, open `/super-admin/plans?lang=en&qa=v151-query-en-<timestamp>` → final EN/LTR.
2. With stored EN, open `/super-admin/plans?lang=ar&qa=v151-query-ar-<timestamp>` → final AR/RTL.

This proves explicit handoff wins during Plans boot.

## Continue Full Audit

Only if Evolution, Tara, Plans Catalog EN/AR, and Plan Editor EN/AR all PASS.

Continue:
1. Company Overrides EN/AR
2. Commercial EN/AR
3. Billing EN/AR
4. Subscriptions EN/AR
5. Settings EN/AR
6. Source Code EN/AR

At first genuine ordinary untranslated static UI: STOP and record language, route/tab/hash, exact rendered text, selector/attribute, sanitized browser finding, screenshot.

No manual fix. No reset/clean/restore. No production commit/push.

Exclude runtime/domain data: names, emails, IDs, dates/timestamps, URLs/IPs, roles, plan/product/provider names and values, slugs/versions/counts, repo/branch/SHA, masked secrets, raw technical errors.

## Evidence

Create:

`TCRMMT_V151_Evidence.zip`

Include deployment/static/runtime, Evolution/Tara regression, Plans EN/AR URL+language-state proof, Plans Catalog/Editor audits, next Full Audit blocker if any, screenshots.

NO COMMIT. NO PUSH.

Upload Final Report + Evidence ZIP to ChatGPT session exactly:

`TCRMMMT`
