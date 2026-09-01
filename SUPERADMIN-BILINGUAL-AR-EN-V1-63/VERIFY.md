# TCRMMT Super Admin Bilingual V1.63 — Company Profile UX Rebuild

## Purpose

V1.62 deployed successfully but browser evidence still showed the Company Profile drawer visually broken:

- English and Arabic ordinary UI mixed in the same drawer.
- Header/tabs were not consistently localized.
- user emails/labels visually overlapped or ran together.
- Last Login / role / status metadata collided.
- user actions were crowded.
- the Users area did not behave like a stable production UI.

V1.63 is a focused Company Profile drawer UX rebuild. It keeps all existing controls, event listeners, runtime data and backend behavior intact.

## Scope

Patch repository branch:

`superadmin-bilingual-ar-en-v1-63`

Folder:

`SUPERADMIN-BILINGUAL-AR-EN-V1-63`

Production target:

`/var/www/TCRMMT`

V1.63 itself may modify exactly:

`server/superAdminUiPolish.ts`

It must not modify:

- `server/_core/index.ts`
- provisioning code
- tenant databases
- migrations
- API behavior
- tenant/user/company runtime values

## Required base

Production must already contain:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1_62_COMPANY_PROFILE_USERS_AR_LAYOUT_CLOSURE`

If missing, STOP.

## Apply

Run:

`python3 apply_superadmin_bilingual_v1_63.py`

twice.

First run must print exactly:

`Applied Super Admin Bilingual V1.63 Company Profile UX rebuild.`

Second run must print exactly:

`Super Admin bilingual V1.63 Company Profile UX rebuild already applied; no changes made.`

Second run must be a true no-op.

## Build gates

Run:

- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

Built runtime must contain:

- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_63_COMPANY_PROFILE_UX_REBUILD`
- `SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V163`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V163`
- `/super-admin/bilingual-v163.js`
- `superadmin-bilingual-v163`

## Restart

After all gates pass, restart only:

`tamiyouz-crm`

Do not restart the provisioning worker.

## Browser QA — mandatory

Use an authenticated Super Admin session.

Open:

`/super-admin#tenants`

Open Company Profile for a tenant, then Users.

### UX requirements

The drawer must:

- have stable width and vertical scrolling;
- never horizontally clip content;
- have a clean header;
- have a distinct company summary/hero block;
- have tabs that wrap safely;
- render the Users area as separated visual cards;
- isolate each email on its own visual line;
- render long emails with safe wrapping;
- keep email direction LTR even in Arabic;
- separate role/status/last-login metadata;
- keep form controls full-width where appropriate;
- keep action buttons in a wrapped action row;
- eliminate visible text overlap;
- eliminate stacked/concatenated email presentation;
- preserve all existing button actions.

### Arabic mode

Ordinary UI must be Arabic, including:

- ملف الشركة
- عرض شامل لبيانات الشركة والاشتراك والفواتير.
- صحة الحساب N%
- فترة تجريبية
- الدخول كمسؤول الشركة
- نظرة عامة
- المستخدمون
- الاشتراك
- الفواتير والمدفوعات
- سجل الشركة
- حسابات الشركة
- تحديث
- مسؤول
- نشط
- آخر تسجيل دخول
- حفظ الدور
- كلمة مرور جديدة
- إيقاف الحساب

Runtime values must remain untouched:
company name, company/user emails, tenant path, health number, timestamps, ids, status values that are data, plans and billing values.

Required:

`COMPANY PROFILE V1.63 AR UX: PASS`

### English mode

Switch the same drawer to English.

Required ordinary UI:

- Company Profile
- Smart view of company, subscription, and billing data.
- Health N%
- Trialing
- Sign in as Company Admin
- Overview
- Users
- Subscription
- Billing & Payments
- Company Log
- Company Accounts
- Refresh
- Admin
- Active
- Last Login
- Save role
- New password
- Suspend

No Arabic ordinary UI leakage.

Required:

`COMPANY PROFILE V1.63 EN UX: PASS`

## Functional smoke

Verify these existing actions are still clickable/usable without errors:

- tab switching
- Refresh
- role select/change UI
- Save role
- New password
- Suspend
- Sign in as Company Admin

Do not actually suspend a user merely for QA. If the button would make a destructive change, verify it is enabled/wired without confirming the destructive action.

## Stop conditions

STOP without additional repair if:

- any build gate fails;
- V1.62 marker is missing;
- V1.63 modifies another source file;
- browser console shows a new V1.63 runtime error;
- drawer actions are broken;
- auth is unavailable.

If auth is unavailable, report:

`BROWSER QA BLOCKED BY AUTH`

Do not fabricate authentication.

## Evidence

Create:

`TCRMMT_V163_COMPANY_PROFILE_UX_REBUILD_Evidence.zip`

Include:

- production HEAD before
- pre-existing git status
- patch first/second outputs
- V1.63 diff
- build gate results
- runtime marker checks
- PM2 restart evidence
- Arabic screenshot
- English screenshot
- browser console errors if any
- Arabic UX result
- English UX result
- functional smoke result
- confirmation provisioning worker unchanged
- confirmation no DB changes
- confirmation no migrations
- confirmation no production commit/push

Upload Final Report + Evidence ZIP to ChatGPT session exactly:

`TCRMMMT`
