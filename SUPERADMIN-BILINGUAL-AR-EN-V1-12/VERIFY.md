# Super Admin Bilingual V1.12 — Companies EN Closure Verification

Target: `/var/www/TCRMMT`

## Hard rules
- No reset / clean / restore.
- No manual code edits.
- No commit / push.
- Only `server/superAdminUiPolish.ts` may change.
- V1.11 marker must exist before apply.
- Apply the official patch once, then a second time to prove idempotency.

## Static gates
1. `git status --short`
2. Apply `apply_superadmin_bilingual_v1_12.py`
3. Apply it again; second run must report already applied/no changes.
4. `git diff --check`
5. `npm run check`
6. `npm run build`
7. `dist/index.js` must contain:
   - `SUPER_ADMIN_BILINGUAL_AR_EN_V1_12_COMPANIES_EN_CLOSURE`
   - `SUPER_ADMIN_BILINGUAL_RUNTIME_V112`
   - `/super-admin/bilingual-v112.js`
   - `superadmin-bilingual-v112`
8. Restart only `tamiyouz-crm` after all gates pass.

## Runtime asset gate
Direct Node and Public HTTPS for `/super-admin/bilingual-v112.js?v=superadmin-bilingual-v112` must return HTTP 200, JavaScript content type, V112 runtime marker, and no-store headers.

## Browser gates
Use fresh browser context and cache disabled.
- Runtime V112.
- EN/LTR default.
- EN → AR → EN works.
- EN and AR refresh persistence work.
- Topbar and dock language controls remain present.

## Regression gates
Before Companies:
- Overview EN must remain `NONE FOUND`.
- Overview AR must remain `NONE FOUND`.

## Companies EN closure gate
Switch Companies to English, wait at least 2 seconds, and scan visible text plus visible `placeholder`, `title`, and `aria-label`.
The following V1.11 findings must be absent:
- `المعروض`
- `فلاتر الشركات`
- `البحث والفلاتر`
- `اعثر على الشركة المطلوبة بسرعة.`
- `اسم الشركة، المسار أو البريد`
- `From date الإنشاء`
- `To date الإنشاء`
- `عدد الصفوف`
- `مسح الفلاتر`
- `حفظ العرض`
- `الحالة، Plan، الصحة والإجراءات.`
- `يمكن التمرير أفقياً عند الحاجة`
- `المسار`
- `الصحة`
- `متبقي`
- any `Server-side pagination · N سجل`

Expected pagination in English: `Server-side pagination · N records`.

Exclude only real company/user data, emails, IPs, IDs, URLs, slugs, product/integration names, repository/branch/commit values, and raw technical identifiers.

If any ordinary Arabic static UI remains in Companies EN, record UNIQUE exact strings, selectors/attributes, screenshot, then STOP. Do not fix.

## Companies AR regression
If Companies EN passes, switch Companies to Arabic and verify no ordinary static English UI remains after allowed exclusions. Dynamic pagination should be Arabic.

## Continue full audit only if Companies EN + AR pass
Continue EN + AR for:
- Tenant Details
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
- Settings / Source Code

Stop on first untranslated static UI finding and report UNIQUE strings. No manual fixes.

## Responsive matrix
Only after translation audit is clean, test EN + AR at 1440×900, 1024×768, 768×900, and 390×844. Require 0 horizontal overflow, no clipping, no overlap.

## Final acceptance strings
- `RUNTIME V112: PASS`
- `LANGUAGE CONTROL LIFECYCLE: PASS`
- `PERSISTENCE: PASS`
- `OVERVIEW EN STATIC UI: NONE FOUND`
- `OVERVIEW AR STATIC UI: NONE FOUND`
- `COMPANIES EN STATIC UI: NONE FOUND`
- `COMPANIES AR STATIC UI: NONE FOUND`
- `UNTRANSLATED STATIC UI: NONE FOUND`
