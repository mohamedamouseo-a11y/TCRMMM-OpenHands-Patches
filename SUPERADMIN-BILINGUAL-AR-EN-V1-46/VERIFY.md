# TCRMMT V1.46 — Evolution direct hash restore after capability load

Target: `/var/www/TCRMMT`

## Scope

Functional routing/runtime fix only.

V1.44 remains the active bilingual runtime. V1.45/V1.46 do **not** create a new bilingual JS asset.

Expected tracked production changes after apply:
- `server/superAdminUiPolish.ts` — existing cumulative V1.44 bilingual changes
- `server/_core/index.ts` — existing V1.45 + new V1.46 direct/hash routing fix

No other tracked files may change.

Do not manually edit production source. Do not reset, clean, restore, commit, or push.

## Why V1.46 exists

V1.45 correctly added an Evolution loader after `loadAccount()`, but initial page routing can evaluate an owner-only `#evolution-api` request before owner capability is known. `goToSection()` then falls back to Overview and rewrites the hash to `#overview`. By the time V1.45 checks `location.hash`, the original direct request has already been lost.

V1.46 captures the initial hash before `initPlatformPageMode()`, then after `loadAccount()` restores `sec-evolution-api` and performs one read-only Evolution loader cycle.

## Preflight

```bash
cd /var/www/TCRMMT
git status --short
grep -c 'SUPER_ADMIN_EVOLUTION_DIRECT_HASH_LOADER_V145' server/_core/index.ts
grep -c 'SUPER_ADMIN_EVOLUTION_DIRECT_HASH_RESTORE_V146' server/_core/index.ts
```

V1.45 prerequisite must exist.
V1.46 must not exist before first apply.

## Apply twice

```bash
python3 apply_superadmin_bilingual_v1_46.py
python3 apply_superadmin_bilingual_v1_46.py
```

Expected:

1. `Applied Super Admin Evolution V1.46 direct hash restore.`
2. `Super Admin Evolution V1.46 direct hash restore already applied; no changes made.`

## Static gates

```bash
git status --short
git diff --check
npm run check
npm run build
```

All must pass.

Allowed tracked modified files only:
- `server/superAdminUiPolish.ts`
- `server/_core/index.ts`

Confirm V1.46 marker in both:

```bash
grep -c 'SUPER_ADMIN_EVOLUTION_DIRECT_HASH_RESTORE_V146' server/_core/index.ts
grep -c 'SUPER_ADMIN_EVOLUTION_DIRECT_HASH_RESTORE_V146' dist/index.js
```

## Restart and stale-process guard

Restart only:

```bash
pm2 restart tamiyouz-crm
```

Prove new PID process start time is strictly AFTER current `dist/index.js` mtime.
If stale: STOP.

Poll port 3002 for readiness for at most 90 seconds.

## Runtime asset gate — IMPORTANT

V1.46 is NOT a bilingual-runtime version.

Do **not** request:
- `/super-admin/bilingual-v145.js`
- `/super-admin/bilingual-v146.js`

The active bilingual runtime remains V1.44.

Check each URL three times:

- `http://127.0.0.1:3002/super-admin/bilingual-v144.js?v=superadmin-bilingual-v144`
- `https://tcrmmm.tamiyouz.com/super-admin/bilingual-v144.js?v=superadmin-bilingual-v144`

Each must be:
- HTTP 200
- JavaScript Content-Type
- `Cache-Control: no-store`
- contain `SUPER_ADMIN_BILINGUAL_RUNTIME_V144`
- NOT HTML fallback

If V1.44 runtime asset fails, STOP.

## Primary V1.46 direct-navigation browser gate

Use a completely fresh authenticated browser context with cache disabled.

Open directly, without first visiting Overview and without clicking Evolution nav:

`https://tcrmmm.tamiyouz.com/super-admin?qa=v146-direct-<timestamp>#evolution-api`

Do not click Evolution nav.
Do not click Refresh.
Do not perform any mutating action.
Do not read secret values.

Required after account capability resolves:

1. Final `location.hash` = `#evolution-api`
2. Active section = `sec-evolution-api`
3. Evolution section visible
4. `GET /api/super-admin/evolution-api/settings` is sent automatically
5. Settings request returns HTTP 200
6. Initial placeholder state (`Not configured / Not saved / Checking...`) is replaced by the real current state
7. No uncontrolled duplicate request loop

Record exact request count and timings.

## Hash away/back gate

After the direct gate passes:

1. Change hash/navigation to a safe non-mutating section such as `#overview`.
2. Then navigate back to `#evolution-api`.
3. Confirm exactly one normal loader cycle occurs and finishes.
4. No duplicate uncontrolled loop.

## Evolution bilingual regression

V1.44 bilingual runtime remains authoritative.

Verify Evolution API EN then AR using the existing V1.44 canonical gates.

### EN

`lang=en`, `dir=ltr`

Required:
- `#evolutionConnectionBadge` = `Configured and ready`
- `#evolutionApiTokenHint` begins `Saved: ` and preserves masked suffix
- `#evolutionWebhookSecretHint` begins `Saved: ` and preserves masked suffix
- `#evolutionManagedCapability` = `Automatic setup is available on the server. The service file will be updated and Evolution API restarted safely.`
- previous V1.40–V1.43 canonical English labels remain correct
- secret placeholders remain `Leave blank to keep the current value`

Expected:

`EVOLUTION API EN STATIC UI: NONE FOUND`

### AR

`lang=ar`, `dir=rtl`

Required:
- `#evolutionConnectionBadge` = `مُعد وجاهز`
- saved hints begin `محفوظ: ` while preserving masked suffix
- `#evolutionManagedCapability` = `الإعداد التلقائي متاح على السيرفر. سيتم تحديث ملف الخدمة وإعادة تشغيل Evolution API بأمان.`
- enable label = `تفعيل تكامل Evolution API`
- secret placeholders = `اتركه فارغًا للاحتفاظ بالقيمة الحالية`

Expected:

`EVOLUTION API AR STATIC UI: NONE FOUND`

## Continue Full Audit

If all above pass, continue EN then AR:

1. Tara APIs
2. Plans Catalog
3. Plan Editor
4. Company Overrides
5. Commercial
6. Billing
7. Subscriptions
8. Settings
9. Source Code

At the first genuine ordinary untranslated static UI: STOP.

Do not fix it manually.

Record:
- language
- page/hash
- exact text
- untranslated segment
- selector/attribute
- raw browser finding
- screenshot

Exclude runtime/domain data, including names, emails, IDs, paths, tenant/product/plan values, roles, dates/timestamps, URLs, IPs, repo/branch/SHA, event payloads, masked secret values, and raw technical errors.

## Evidence

Create:

`TCRMMT_V146_Evidence.zip`

Include:
- preflight
- first apply + second no-op
- tracked scope
- static gates
- source/dist marker
- restart/stale proof
- V1.44 runtime asset Direct/Public 3x
- direct `#evolution-api` request count/status/timing
- final hash + active section
- hash-away/back request count
- Evolution EN/AR
- Full Audit progress
- first genuine blocker if any
- screenshots
- final report

No commit.
No push.

VERY IMPORTANT:

Upload the final report and `TCRMMT_V146_Evidence.zip` inside ChatGPT Session exactly named:

`TCRMMMT`
