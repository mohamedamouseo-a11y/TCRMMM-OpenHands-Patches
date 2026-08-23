# TCRMMT Super Admin Bilingual V1.17 — Users EN Full Closure

Target: `/var/www/TCRMMT`

Patch: `apply_superadmin_bilingual_v1_17.py`

## Purpose
Close all ordinary Users-page English-mode Arabic strings visible in the V1.16 raw browser evidence and screenshot in one pass, while preserving the already accepted Users AR headers and prior Overview / Companies / Tenant Details closures.

## Required baseline
The source must contain:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1_16_USERS_AR_HEADER_CLOSURE`

## Apply
Run the patch twice. First run must apply. Second run must report already applied / no changes.

Only this production source file may change:

`server/superAdminUiPolish.ts`

## Static gates
Run:

- `git diff --check`
- `npm run check`
- `npm run build`

All must pass.

Before restart, `dist/index.js` must contain:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V117`
- `/super-admin/bilingual-v117.js`
- `superadmin-bilingual-v117`

## Runtime asset
Direct Node and public asset `/super-admin/bilingual-v117.js?v=superadmin-bilingual-v117` must return JavaScript HTTP 200, no-store headers, and `SUPER_ADMIN_BILINGUAL_RUNTIME_V117`.

## Users EN closure targets
In English mode the following Arabic/mixed static strings must not remain:

- `مستخدمو الشركات`
- dynamic `N حساب مسجل عبر N شركة`
- `حسابات نشطة`
- `الاسم، البريد أو الدور`
- `كل الأدوار`
- `محذوف`
- `عرض النتائج`
- `آخر LOGIN`
- `بيانات الLOGIN`
- `كلمة مرور جديدة`
- `إيقاف`
- `مفعّلة`
- `متوقف`

Expected English equivalents include:

- `Company Users`
- `N registered accounts across N companies`
- `Active accounts`
- `Name, email, or role`
- `All roles`
- `Deleted`
- `Show results`
- `Last Login`
- `Login Details`
- `New password`
- `Suspend`
- `Enabled`
- `Suspended`

## Regression gates
Re-run Users AR after Users EN and confirm the V1.16 targets remain Arabic:

- `المستخدمون والصلاحيات`
- `المستخدمون المركزيون`

Also confirm previously accepted Overview, Companies, and Tenant Details regressions before continuing the remaining full audit.

## Stop rule
If any ordinary untranslated static UI appears, do not fix manually. Record exact text, language, page, selector/attribute, screenshot, and stop.

No commit or push.
