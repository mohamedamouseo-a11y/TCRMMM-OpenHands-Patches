# TCRMMT Super Admin — Phase 1 Verification

## Scope
Design System + App Shell only. No API, DB, auth, permission, route, or business-logic changes.

## Required checks
1. `python3 SUPERADMIN-PHASE1-ENTERPRISE-SHELL-V1/apply_phase1.py` completes successfully and prints a backup path.
2. `npm run check` succeeds, or any pre-existing unrelated TypeScript errors are explicitly separated from Phase 1.
3. `npm run build` succeeds.
4. Restart only the TCRMMT web application process after a successful build.
5. Super Admin login still succeeds.
6. Verify every existing Super Admin navigation destination remains reachable:
   - Overview / Command Center
   - Companies
   - Users
   - Plans & Limits
   - Platform Admins
   - Actions & Analytics
   - Activity
   - Audit Log
   - GitHub Sync
   - Evolution API
   - Tara APIs
   - System Settings
7. Verify owner-only items remain owner-only.
8. Verify sidebar collapse/expand works and persists after refresh.
9. Verify desktop at 1440x900 and one mobile/narrow viewport.
10. Verify light and dark themes.
11. Verify no horizontal page overflow and no clipped sidebar footer/logout action.
12. Capture screenshots of: Overview, Companies, Users, one Integrations page, System Settings, collapsed sidebar.

## Stop conditions
Stop and report before restart if build fails or if the patch cannot identify the expected Super Admin shell signatures. Do not improvise edits to auth, DB, routes, or APIs.
