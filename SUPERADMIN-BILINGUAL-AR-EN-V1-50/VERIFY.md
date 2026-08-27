# TCRMMT Super Admin Bilingual V1.50 — VERIFY

## Scope

V1.50 is a narrow bilingual runtime-ordering fix.

Evidence established:
- V1.49 deploy/runtime is healthy.
- Tara EN can end with `html lang="en" dir="ltr"` while ordinary Tara static UI is still Arabic.
- The standalone runtime `sweep()` is page-aware and V1.47 Tara canonicalization is inside it.
- The existing body `MutationObserver` does **not** watch the root language attributes.
- The Tara standalone page runs its own inline async `loadTenants()/loadRows()/render()` lifecycle before/around the deferred bilingual runtime.

V1.50 does not change Tara APIs, data, secrets, persistence, or integration business logic.
It only makes the bilingual runtime schedule another `sweep()` when the root `<html>` language state changes.

Target:
`/var/www/TCRMMT/server/superAdminUiPolish.ts`

Marker:
`SUPER_ADMIN_BILINGUAL_AR_EN_V1_50_TARA_LANGUAGE_ATTRIBUTE_RESWEEP`

Active runtime:
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V150`
- `/super-admin/bilingual-v150.js`
- cache key `superadmin-bilingual-v150`

## Hard safety rules

- Use the supplied patch script only.
- No manual source edits.
- No reset / clean / restore.
- No main-project commit or push.
- Restart only `tamiyouz-crm`.
- Do not read, expose, or modify secret values.
- Tara testing is read-only; opening/closing Add Integration modal is permitted, submit/test/disable/delete are prohibited.

## Preflight

```bash
cd /var/www/TCRMMT
git status --short
```

Only the cumulative intended tracked modifications are allowed:
- `server/superAdminUiPolish.ts`
- `server/_core/index.ts`

STOP on any unrelated tracked modification.

Confirm:
- V1.49 marker exists in `server/superAdminUiPolish.ts`
- V1.50 marker is absent before first apply.

## Apply twice

```bash
python3 apply_superadmin_bilingual_v1_50.py
python3 apply_superadmin_bilingual_v1_50.py
```

Expected first:
`Applied Super Admin Bilingual V1.50 Tara language-attribute resweep runtime.`

Expected second:
`Super Admin bilingual V1.50 Tara language-attribute resweep already applied; no changes made.`

## Static gates

```bash
git diff --check
npm run check
npm run build
```

All must PASS.

Confirm source and `dist/index.js` contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_50_TARA_LANGUAGE_ATTRIBUTE_RESWEEP`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V150`
- `/super-admin/bilingual-v150.js`
- `superadmin-bilingual-v150`
- root observer attribute filter containing `lang`, `dir`, `data-sa-lang`.

## Restart

Record current `dist/index.js` mtime epoch and current PM2 PID/start time.

Restart only:
```bash
pm2 restart tamiyouz-crm
```

Stale-process guard:
new PM2 start epoch must be strictly greater than current `dist/index.js` mtime.
Otherwise STOP.

Port 3002 readiness must succeed within 90 seconds.

## Runtime asset

Direct 3x:
`http://127.0.0.1:3002/super-admin/bilingual-v150.js?v=superadmin-bilingual-v150`

Public 3x:
`https://tcrmmm.tamiyouz.com/super-admin/bilingual-v150.js?v=superadmin-bilingual-v150`

Each:
- HTTP 200
- JavaScript Content-Type
- Cache-Control no-store
- marker `SUPER_ADMIN_BILINGUAL_RUNTIME_V150`
- not HTML fallback.

## Regression — Evolution

Fresh authenticated browser, cache disabled.

Read-only:
1. Direct `/super-admin#evolution-api`
2. Confirm active Evolution section and exactly one initial settings loader cycle.
3. Navigate away then back; exactly one additional loader cycle.
4. EN canonical static UI.
5. AR canonical static UI.

Expected:
- `EVOLUTION API EN STATIC UI: NONE FOUND`
- `EVOLUTION API AR STATIC UI: NONE FOUND`

## PRIMARY — Tara EN ordering regression

Use a normal authenticated navigation sequence.

Important: explicitly test the sequence that previously failed.

1. Start in Super Admin AR.
2. Visit Tara AR once and confirm canonical Arabic.
3. Return to main Super Admin.
4. Switch to EN using the normal product language mechanism.
5. Confirm main page is `lang=en`, `dir=ltr`.
6. Navigate normally to `/super-admin/tara-integrations`.
7. Do not refresh merely to force translation.

Final Tara DOM must be:
- `lang=en`
- `dir=ltr`

And ordinary static UI must be canonical English, including:
- `Platform Administration · Tara`
- `Tara Integrations`
- selected-company subtitle in English while preserving company name
- `Back to Admin Console`
- `Bahgat Settings`
- `Add Integration`
- `Company`
- `Refresh Data`
- owner-only audit note
- stat labels/hints
- `Integrations and APIs`
- empty/card static UI.

Required exact blockers from V1.49 must be absent:
- `تكاملات تارا`
- `إضافة تكامل`
- `تحديث البيانات`
- `إجمالي التكاملات`
- `التكاملات والواجهات البرمجية`

Expected:
`TARA APIs EN STATIC UI: NONE FOUND`

### Root-language observer proof

Without changing production source, use read-only DevTools observation if available.

Capture that a transition of any of:
- `html lang`
- `html dir`
- `html data-sa-lang`

causes a subsequent bilingual sweep / translated final state.

Do not require breakpoints if browser automation cannot preserve them; final DOM + source marker + root observer source proof are sufficient.

## Tara modal EN

Open Add Integration modal only; do not submit.

Expected canonical English labels and placeholder:
- Add Integration
- Provider
- Integration status
- Basic settings
- Connection data
- API key
- Leave blank to keep the saved value
- Sensitive data is encrypted before storage.
- Save securely
- Close

Close modal.

No mutation.

## Tara AR reverse

Switch normally to AR and revisit Tara.

Confirm:
- `lang=ar`
- `dir=rtl`
- canonical Arabic page and modal.

Expected:
`TARA APIs AR STATIC UI: NONE FOUND`

## Plans V1.49 regression

Now run the V1.49 primary Plans gates that were previously blocked by Tara.

EN:
- `#status` exactly:
  `Ready — all operational controls start safely and can be enabled progressively.`
- empty state if present:
  `Select a plan to view its details`
- no mixed Arabic/English variant.

Expected:
- `PLANS CATALOG EN STATIC UI: NONE FOUND`
- `PLAN EDITOR EN STATIC UI: NONE FOUND`

AR reverse:
- status canonical Arabic
- empty state canonical Arabic

Expected:
- `PLANS CATALOG AR STATIC UI: NONE FOUND`
- `PLAN EDITOR AR STATIC UI: NONE FOUND`

No Save / Clone / Publish.

## Continue Full Audit

If all above pass, continue in this exact order:

1. Company Overrides EN/AR
2. Commercial EN/AR
3. Billing EN/AR
4. Subscriptions EN/AR
5. Settings EN/AR
6. Source Code EN/AR

At the first genuine ordinary untranslated static UI:
STOP and record:
- language
- page/hash/tab
- exact visible text
- untranslated segment
- selector/attribute
- sanitized browser finding
- screenshot.

Do not patch manually.

Exclude domain/runtime values:
names, company names, emails, IDs, counts, dates/timestamps, paths, plan/product/provider/brand values, roles, URLs/IPs, repo/branch/SHA, masked secrets, raw technical errors.

## Evidence

Create:
`TCRMMT_V150_Evidence.zip`

Include:
- apply x2
- static gates
- source/dist markers
- PM2 stale-process proof
- runtime asset Direct/Public 3x
- Evolution regression
- Tara EN failed-sequence regression proof
- Tara EN modal read-only
- Tara AR reverse
- Plans V1.49 EN/AR gates
- continued full audit or first blocker
- final production status.

NO COMMIT.
NO PUSH.

Upload final report and ZIP into ChatGPT session exactly:
`TCRMMMT`
