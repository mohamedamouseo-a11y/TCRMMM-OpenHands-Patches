# TCRMMT Super Admin Bilingual V1.20 — Platform Admins AR Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_20.py` to `/var/www/TCRMMT`.

V1.19 runtime/build/regression gates are already PASS. This patch closes only the first genuine Full Audit blocker found after V1.19:

- Platform Admins / Arabic subtitle:
  - forbidden mixed form: `إدارة حسابات Platform Admin وتوزيع الشركات`
  - expected canonical Arabic: `إدارة حسابات مسؤولي المنصة وتوزيع الشركات`

The patch preserves the English canonical phrase:
`Manage Platform Admin accounts and company assignments`

Do not translate user names, company names, emails, dates, IDs, paths, plan/product values, or runtime/domain data.

## Preconditions
Required source marker:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_19_COMPANIES_AR_PLAN_CLOSURE`

## Safety
Before apply run `git status --short`.

Forbidden:
- reset / clean / restore
- manual source edits
- commit / push
- DB / migrations / Nginx changes
- unrelated PM2 changes

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_20.py`

twice.

First run must print:
`Applied Super Admin Bilingual V1.20 Platform Admins AR closure runtime.`

Second run must be no-op.

## Static gates
Only this worktree file may change:
`server/superAdminUiPolish.ts`

Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

Dist must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_20_PLATFORM_ADMINS_AR_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V120`
- `/super-admin/bilingual-v120.js`
- `superadmin-bilingual-v120`

## Restart / readiness
Only after all static/build/dist gates PASS:
`pm2 restart tamiyouz-crm`

Use readiness polling for port `3002` for up to 90 seconds. Do not treat a fixed short sleep as a failure gate.

Verify direct and public:
- `/super-admin`
- `/super-admin/bilingual-v120.js?v=superadmin-bilingual-v120`

Required:
- HTTP 200
- JavaScript content type for runtime asset
- `no-store` cache headers
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V120` in asset

## Browser QA
Fresh browser context, cache disabled.

### Regression gates first
Reconfirm:
- Users EN / AR
- Overview EN / AR
- Companies EN / AR
- Tenant Details EN / AR

Any regression = FAIL and STOP.

### Platform Admins AR — blocking gate
Open `#platform-admins` in Arabic and wait for translation/runtime stabilization.

Required:
- `lang=ar`
- `dir=rtl`
- subtitle exact canonical Arabic:
  `إدارة حسابات مسؤولي المنصة وتوزيع الشركات`

Forbidden ordinary static forms:
- `إدارة حسابات Platform Admin وتوزيع الشركات`
- `إدارة حسابات مسؤول المنصة وتوزيع الشركات`

Scan visible text plus `placeholder`, `title`, and `aria-label` for ordinary English leakage. Exclude only genuine runtime/domain data.

Expected result:
`PLATFORM ADMINS AR STATIC UI: NONE FOUND`

### Platform Admins EN
Switch to English and verify:
- `lang=en`
- `dir=ltr`
- no ordinary Arabic static UI leakage
- English subtitle is coherent and contains no mixed Arabic/English form

Expected result:
`PLATFORM ADMINS EN STATIC UI: NONE FOUND`

## Continue Full Audit
If Platform Admins EN/AR PASS, continue in this order, both EN and AR:
1. Activity
2. Audit Log
3. GitHub Sync
4. Evolution API
5. Tara APIs
6. Plans Catalog
7. Plan Editor
8. Company Overrides
9. Commercial
10. Billing
11. Subscriptions
12. Settings
13. Source Code

At the first genuine ordinary untranslated static UI:
**STOP immediately. Do not fix it manually.**

Record:
- language
- page/hash
- exact text
- untranslated segment
- selector / attribute
- raw browser finding
- screenshot

## Final report
Include:
```text
RUNTIME V120:
USERS EN:
USERS AR:
OVERVIEW EN:
OVERVIEW AR:
COMPANIES EN:
COMPANIES AR:
TENANT DETAILS EN:
TENANT DETAILS AR:
PLATFORM ADMINS EN:
PLATFORM ADMINS AR:
NEXT TRANSLATION BLOCKER:
UNTRANSLATED STATIC UI:
```

Send ZIP evidence and stop.

**No commit or push.**
