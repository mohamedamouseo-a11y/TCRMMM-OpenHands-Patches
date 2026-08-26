# TCRMMT Super Admin Bilingual V1.48 — Plans Catalog + Plan Editor Full Static Closure

## Scope

Apply the official patch only to `/var/www/TCRMMT`.

V1.48 changes only:

- `server/superAdminUiPolish.ts`

The cumulative production working tree is expected to retain the previously authorized:

- `server/_core/index.ts`
- `server/superAdminUiPolish.ts`

No other tracked file may be modified.

Do not manually edit source. Do not reset, clean, restore, commit, or push.

## Preflight

```bash
cd /var/www/TCRMMT
git status --short
grep -c 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_47_TARA_APIS_FULL_STATIC_CLOSURE' server/superAdminUiPolish.ts
grep -c 'SUPER_ADMIN_EVOLUTION_DIRECT_HASH_RESTORE_V146' server/_core/index.ts
grep -c 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_48_PLANS_CATALOG_EDITOR_FULL_STATIC_CLOSURE' server/superAdminUiPolish.ts
```

Required before first apply:

- V1.47 marker exists.
- V1.46 direct-hash marker exists.
- V1.48 marker is absent.

## Apply twice

```bash
python3 apply_superadmin_bilingual_v1_48.py
python3 apply_superadmin_bilingual_v1_48.py
```

Expected first output:

`Applied Super Admin Bilingual V1.48 Plans Catalog/Editor full static closure runtime.`

Expected second output:

`Super Admin bilingual V1.48 Plans Catalog/Editor full static closure already applied; no changes made.`

## Static gates

```bash
git status --short
git diff --check
npm run check
npm run build
```

All must pass.

Confirm `dist/index.js` contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_48_PLANS_CATALOG_EDITOR_FULL_STATIC_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V148`
- `/super-admin/bilingual-v148.js`
- `superadmin-bilingual-v148`

## Restart and stale-process guard

Restart only:

```bash
pm2 restart tamiyouz-crm
```

Prove the new PM2 process start time is strictly later than the current `dist/index.js` mtime. If stale, STOP.

Poll port 3002 for readiness for at most 90 seconds.

## Runtime asset V1.48

Test each URL three times:

- `http://127.0.0.1:3002/super-admin/bilingual-v148.js?v=superadmin-bilingual-v148`
- `https://tcrmmm.tamiyouz.com/super-admin/bilingual-v148.js?v=superadmin-bilingual-v148`

Every response must be:

- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- contains `SUPER_ADMIN_BILINGUAL_RUNTIME_V148`
- not HTML fallback

## Regression gates

Fresh authenticated browser, cache disabled.

Re-run read-only:

1. V1.46 direct `#evolution-api` and hash-away/back.
2. Evolution API EN/AR.
3. Tara APIs EN/AR including opening/closing Add Integration modal without submit.

Expected:

- `EVOLUTION API EN STATIC UI: NONE FOUND`
- `EVOLUTION API AR STATIC UI: NONE FOUND`
- `TARA APIs EN STATIC UI: NONE FOUND`
- `TARA APIs AR STATIC UI: NONE FOUND`

Never read secret values and never perform mutating actions.

## Plans Catalog EN — PRIMARY V1.48 GATE

Open fresh:

`https://tcrmmm.tamiyouz.com/super-admin/plans?qa=v148-plans-en-<timestamp>`

Set/confirm:

- `lang=en`
- `dir=ltr`
- Plans tab active

Do not save, clone, publish, assign, or mutate anything.

Verify the visible ordinary static surface is English, including at minimum:

- `Plans & Limits Management`
- `Manage versions, subscriptions, and usage limits`
- `Back to Command Center`
- `Refresh Data`
- safety notice and Show/Hide details
- status/loading copy
- top tabs:
  - `Plans`
  - `Companies & Overrides`
  - `Operations, Subscriptions & Billing`
- Plans intro:
  - `Plans Management`
  - `Plans Catalog`
  - `Manage versions, features, and limits from one clear workspace.`
  - `Version Management`
- list rail:
  - `Plan Versions`
  - `Published, draft, and archived versions.`
  - `Search plans`
  - English search placeholder
  - count grammar such as `<n> versions · <n> published`
  - `No data available.` / `No plans match your search.` when applicable

Plan names, plan slugs, versions, counts, feature catalog names/descriptions, units, and other plan/product/runtime values are domain data and must be preserved/excluded from static translation findings.

Expected:

`PLANS CATALOG EN STATIC UI: NONE FOUND`

## Plan Editor EN — V1.48 GATE

Select/open one existing plan only. This is read-only.

Do NOT click:

- Clone to draft
- Save draft
- Publish version
- any checkbox/select/input intended to persist changes

Verify ordinary static editor UI is English:

- `Select a plan` / selected-plan editor headings
- dynamic subtitle uses `Identifier <slug> · Version <version>`
- `Status`, `Version`, `Companies`
- dynamic company count uses `<n> companies`
- `Arabic name`
- `English name`
- `New version identifier`
- `Version information`
- `Features`
- `Future features are locked and are not currently active.`
- `Limits`
- draft/publish help text
- limit mode options:
  - `Undefined`
  - `Value`
  - `Unlimited`
- status labels:
  - `Published`
  - `Draft`
  - `Archived`
- dynamic feature helper prefixes if present:
  - `Requires:`
  - `Future — cannot be enabled`
- footer buttons:
  - `Clone to draft`
  - `Save draft`
  - `Publish version`
- final editor hint is canonical English

Expected:

`PLAN EDITOR EN STATIC UI: NONE FOUND`

## Plans Catalog + Editor AR

Switch normally to Arabic.

Confirm:

- `lang=ar`
- `dir=rtl`

Re-check Plans Catalog and one selected Plan Editor.

All V1.48 ordinary static labels must return to their canonical Arabic forms.

Dynamic plan names/slugs/versions/counts remain preserved.

Expected:

- `PLANS CATALOG AR STATIC UI: NONE FOUND`
- `PLAN EDITOR AR STATIC UI: NONE FOUND`

## Continue Full Audit

If all V1.48 gates pass, continue in order:

1. Company Overrides EN/AR
2. Commercial EN/AR
3. Billing EN/AR
4. Subscriptions EN/AR
5. Settings EN/AR
6. Source Code EN/AR

At the first genuine ordinary untranslated static UI:

STOP immediately.

Do not manually fix or write code.

Capture:

- language
- page/hash/tab
- exact text
- untranslated segment
- selector/attribute
- raw browser finding
- screenshot

Exclude runtime/domain data including:

- plan names/slugs/versions
- feature/catalog product values
- company names
- emails
- IDs
- counts
- dates/timestamps
- paths/URLs/IPs
- roles
- repo/branch/SHA
- masked secrets
- raw technical errors

## Evidence

Create:

`TCRMMT_V148_Evidence.zip`

Include:

- preflight
- Apply/no-op
- tracked scope
- static gates/build
- V148 source/dist/runtime markers
- PM2 restart + stale guard
- V148 Direct/Public runtime asset 3x each
- Evolution regression
- Tara regression
- Plans Catalog EN/AR
- Plan Editor EN/AR
- Full Audit progress
- first genuine blocker if found
- screenshots
- final report

NO COMMIT.
NO PUSH.

Upload the final report and `TCRMMT_V148_Evidence.zip` inside ChatGPT Session exactly named:

`TCRMMMT`
