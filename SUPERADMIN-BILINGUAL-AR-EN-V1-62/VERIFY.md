# TCRMMT Super Admin Bilingual V1.62 — Company Profile Users Arabic/Layout Closure

## Purpose

Fix the Company Profile drawer on `/super-admin#tenants` shown in the supplied screenshot.

The patch is intentionally scoped to the Company Profile drawer only. It fixes:

- mixed Arabic/English static copy;
- `Health N%` / `Last Login` dynamic labels while preserving the runtime value;
- Company Profile tabs and action buttons;
- Company Accounts helper text;
- email/text wrapping and overlapping rows inside the Users tab.

It does **not** change company names, emails, tenant paths, health percentage values, dates/timestamps, roles stored in data, plans, subscriptions, billing data, tenant provisioning, databases, or authentication.

## Patch chain

Required previous marker:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1_61_COMMERCIAL_MONETIZATION_FORMS_HARD_CLOSURE`

New marker:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1_62_COMPANY_PROFILE_USERS_AR_LAYOUT_CLOSURE`

Target file only:

`/var/www/TCRMMT/server/superAdminUiPolish.ts`

## Production preflight

From `/var/www/TCRMMT` record, do not clean:

```bash
pwd
git branch --show-current
git rev-parse HEAD
git status --short
```

Expected branch: `master`.

Known pre-existing dirty files may include:

- `scripts/provisioning-schema-contract.mjs`
- `server/_core/index.ts`
- `server/superAdminUiPolish.ts`

Preserve all pre-existing work exactly. Do not reset, clean, restore, checkout, stash, commit, push, or edit unrelated files.

Confirm V1.61 marker exists and V1.62 marker is absent before first apply.

## Apply twice

Run the official script from this patch folder against the production source.

First run must print exactly:

`Applied Super Admin Bilingual V1.62 Company Profile Users Arabic/layout closure.`

Second run must print exactly:

`Super Admin bilingual V1.62 Company Profile Users Arabic/layout closure already applied; no changes made.`

The second run must be an exact no-op.

V1.62 itself may modify only:

`server/superAdminUiPolish.ts`

## Static gates

Run:

```bash
git diff --check
npm run check
npm run build
```

All must PASS.

Confirm built output contains:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_62_COMPANY_PROFILE_USERS_AR_LAYOUT_CLOSURE`
- `SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V162`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V162`
- `/super-admin/bilingual-v162.js`
- `superadmin-bilingual-v162`

## Restart

Only after all gates pass, restart exactly:

```bash
pm2 restart tamiyouz-crm
```

Do **not** restart `tamiyouz-crm-provisioning-worker` for this UI patch.

Do not run tenant retry, provisioning, DB SQL, migrations, or any Hamdi recovery action as part of V1.62.

## Browser QA — Arabic

Use a fresh browser context with cache disabled if authentication is available.

Open:

`/super-admin#tenants`

Open the same Company Profile drawer and select **Users**.

Arabic mode must show ordinary UI copy as Arabic, including:

- `ملف الشركة`
- `عرض شامل لبيانات الشركة والاشتراك والفواتير.`
- `صحة الحساب N%`
- `فترة تجريبية`
- `الدخول كمسؤول الشركة`
- `نظرة عامة`
- `المستخدمون`
- `الاشتراك`
- `الفواتير والمدفوعات`
- `سجل الشركة`
- `حسابات الشركة`
- `لا يتم عرض كلمات المرور الحالية. يمكنك إنشاء كلمة مرور جديدة فقط.`
- `تحديث`
- `مسؤول`
- `نشط`
- `آخر تسجيل دخول`
- `حفظ الدور`
- `كلمة مرور جديدة`
- `إيقاف الحساب`

The runtime health percentage, company name, tenant path, emails, dates/timestamps and other data values must remain unchanged.

### Layout gate

Inside Company Profile > Users:

- no email may overlap another email or label;
- long emails must wrap safely instead of colliding;
- action buttons must wrap with visible spacing;
- tabs must wrap with visible spacing if the drawer is narrow;
- there must be no horizontal text collision or clipped user-account row.

Required finding:

`COMPANY PROFILE USERS AR STATIC/LAYOUT: PASS`

Capture a screenshot of the complete drawer.

## Browser QA — English regression

Switch to English without changing runtime data.

Expected static UI includes:

- `Company Profile`
- `Smart view of company, subscription, and billing data.`
- `Health N%`
- `Trialing`
- `Sign in as Company Admin`
- `Overview`
- `Users`
- `Subscription`
- `Billing & Payments`
- `Company Log`
- `Company Accounts`
- `Refresh`
- `Admin`
- `Active`
- `Last Login`
- `Save role` or the canonical existing capitalization
- `New password`
- `Suspend`

No Arabic static leakage is allowed in the Company Profile drawer in English mode.

Required finding:

`COMPANY PROFILE USERS EN STATIC/LAYOUT: PASS`

## Authentication rule

If the OpenHands browser does not have an authenticated Super Admin session, do not fabricate authentication and do not expose credentials.

Complete static/build/runtime verification, report:

`BROWSER QA BLOCKED BY AUTH`

and stop browser QA. The user can provide a logged-in screenshot afterwards.

## Final evidence

Create:

`TCRMMT_V162_COMPANY_PROFILE_USERS_Evidence.zip`

Include:

- preflight HEAD and git status;
- exact first/second apply outputs;
- V1.62-only diff summary;
- `git diff --check` result;
- `npm run check` result;
- `npm run build` result;
- built/runtime marker checks;
- PM2 restart result for `tamiyouz-crm` only;
- Arabic Company Profile > Users screenshot and findings if authenticated;
- English regression screenshot/findings if authenticated;
- confirmation that no DB/provisioning/Hamdi retry action was performed;
- confirmation that no production commit or push was performed.

Upload the report and evidence ZIP to ChatGPT session exactly:

`TCRMMMT`
