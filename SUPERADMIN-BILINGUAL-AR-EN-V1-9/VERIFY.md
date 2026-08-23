# Super Admin Bilingual V1.9 — Phrase Runtime Verification

Scope: translation engine only. Do not change DB, APIs, Auth, Routes, Permissions, Billing, Subscription logic, Business Logic, or navigation handlers.

1. Run `git status --short`. No reset / clean / restore.
2. Verify `SUPER_ADMIN_BILINGUAL_AR_EN_V1_8_STANDALONE_RUNTIME` exists in `server/superAdminUiPolish.ts`.
3. Apply `apply_superadmin_bilingual_v1_9.py` once. Run it a second time; it must be a no-op.
4. The only modified source file must be `server/superAdminUiPolish.ts`.
5. Run `git diff --check`, `npm run check`, `npm run build`.
6. BEFORE restart, verify `dist/index.js` contains:
   - `SUPER_ADMIN_BILINGUAL_AR_EN_V1_9_PHRASE_RUNTIME`
   - `SUPER_ADMIN_BILINGUAL_RUNTIME_V19`
   - `/super-admin/bilingual-v19.js`
   - `superadmin-bilingual-v19`
7. If all pass, restart only `tamiyouz-crm`.
8. Direct and public asset proof: `/super-admin/bilingual-v19.js?v=superadmin-bilingual-v19` must return HTTP 200 JavaScript, V19 marker, and no-store headers.
9. Use a brand-new browser context with cache disabled. Clear LocalStorage. Runtime must be `SUPER_ADMIN_BILINGUAL_RUNTIME_V19`; default EN/LTR; visible language controls; EN→AR→EN and persistence must pass.
10. Start Translation Audit with authenticated Overview EN. Wait 2 seconds after render. Scan visible text + placeholder + title + aria-label.
11. If Overview EN has findings, report UNIQUE untranslated static strings (not only element count), each with exact text, selector/attribute, and screenshot. Do not fix manually.
12. Only if Overview EN passes, test Overview AR, then continue: Companies, Tenant Details, Users, Platform Admins, Activity, Audit Log, GitHub Sync, Evolution API, Tara APIs, Plans Catalog, Plan Editor, Company Overrides, Commercial, Billing, Subscriptions, Settings, Source Code — EN + AR.
13. Exclude only real data: company/user names, emails, IDs, URLs, slugs, tokens, repository/branch/commit values, product names, raw technical identifiers.
14. Responsive EN + AR: 1440×900, 1024×768, 768×900, 390×844; horizontal overflow 0; no clipping/overlap.
15. Final acceptance requires exactly: `UNTRANSLATED STATIC UI: NONE FOUND` plus runtime/lifecycle/persistence PASS.
16. No commit or push.
