# Super Admin Bilingual AR/EN V1.2 — VERIFY

## Scope

Target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`

Marker: `SUPER_ADMIN_BILINGUAL_AR_EN_V1_2`

This is a presentation/localization-only corrective patch based on the V1.1 live audit. It must not change DB, APIs, Auth, Routes, Permissions, Billing, Subscription logic, Business Logic, Navigation handlers, or application data.

## Preconditions

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1` exists.
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_1` exists.
- The worktree may already contain the expected modified `server/superAdminUiPolish.ts` from V1/V1.1. Do not reset/restore it.

## Apply

Run the patch once only:

```bash
python3 apply_superadmin_bilingual_v1_2.py
```

Expected output:

`Applied Super Admin Bilingual Arabic / English V1.2 coverage corrective patch.`

Then:

```bash
git diff --check
npm run check
npm run build
```

All must PASS before restart.

Restart only:

```bash
pm2 restart tamiyouz-crm
```

## Required language behavior

English:
- `html.lang === "en"`
- `html.dir === "ltr"`

Arabic:
- `html.lang === "ar"`
- `html.dir === "rtl"`

Persistence key:

`tcrm-super-admin-language`

Language switching must be instant and survive refresh.

## V1.2 regression gates

### Arabic Login

At `1440x900` verify all of these are Arabic UI copy:

- `إدارة المنصة، ببساطة.`
- `تحكم آمن ومتعدد الشركات في منظومة TCRMMT بالكامل.`
- Theme -> `المظهر`
- Help -> `مساعدة`
- OWNER ONLY generated suffix -> `للمالك فقط`

TAMIYOUZ and TCRMMT remain product names.

### English Settings at 390x844

Must show English, not Arabic:

- `Appearance, Account, and Download Source Code.`
- `🌙 Dark`
- `☀ Light`
- `Download a real copy of the current SaaS source.`
- `Loading source data...`

### English GitHub Sync

At `1440x900` the actual active section must be `#sec-github` and the surface must not contain ordinary Arabic helper/status copy.

Specifically verify English for:

- Repository Connection Details
- Current repository status, GitHub PAT, and selected branch.
- Technical details
- View details
- Loading GitHub status...
- Repository Information
- Connection & PAT Status
- Branch & Revision Information
- Checking sync status...

Technical terms GitHub / PAT / Repository / Branch / Commit / Push may remain English.

### English Evolution API

At `1440x900` and `768x900`, actual active section must be `#sec-evolution-api`.

Ordinary helper/status copy must be English, including configuration, loading, safe-secret, automatic setup and generated-data controls.

Evolution API, API Token, Base URL and Webhook are technical/product labels and may remain English.

### Plans / Commercial

English mode must translate the audited static Arabic copy including:

- View details
- Select a plan to view its details
- Active subscriptions
- Pending requests
- Complete commercial and operational details.
- Activities
- Active automations
- Active Webhooks
- recurring workflow descriptions

Do not translate plan names, company names, slugs, IDs, stored values, URLs, emails, tokens, or product identifiers.

## Full translation audit

Re-run the static UI scanner across:

- Login / Forgot / Reset
- Overview
- Companies
- Users
- Platform Admins
- Activity
- Audit Log
- GitHub Sync
- Evolution API
- Tara APIs
- Plans Catalog
- Plan Editor
- Company Overrides
- Commercial / Billing / Subscriptions
- Settings / Account / Appearance / Source Code
- Tenant Details

Test both EN and AR.

For every candidate, exclude only legitimate record/data values and technical identifiers. Static interface copy in the wrong language is a FAIL.

Final report must include exactly one section:

`UNTRANSLATED STATIC UI`

Acceptance requires:

`NONE FOUND`

If anything remains, do not fix it manually. Record exact visible text, language, surface, selector/id/class, screenshot and the intended translation.

## Responsive

Test EN + AR at:

- 1440x900
- 1024x768
- 768x900
- 390x844

For each record:

- innerWidth
- clientWidth
- scrollWidth
- page horizontal overflow

Required page overflow: `0px`.

No clipping, overlap, or off-screen primary controls.

## Screenshots

Minimum evidence:

1. Login EN 1440
2. Login AR 1440
3. Overview EN 1440
4. Overview AR 1440
5. Settings EN 390
6. Settings AR 390
7. GitHub Sync EN 1440
8. Evolution API EN 1440
9. Plans Catalog EN 1440
10. Commercial EN 1440

## Safety

- No Commit.
- No Push.
- No DB writes.
- No Save/Apply destructive operations.
- No Download/Export needed for QA.
- Use synthetic invalid login only for auth state testing.
