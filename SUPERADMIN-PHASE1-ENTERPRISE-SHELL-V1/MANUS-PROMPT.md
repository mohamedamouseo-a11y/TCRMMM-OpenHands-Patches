# Manus Prompt — TCRMMT Super Admin Phase 1

Apply the prepared Phase 1 patch from the public patch repository only.

Repository: `mohamedamouseo-a11y/TCRMMM-OpenHands-Patches`
Branch: `phase1-superadmin-enterprise-shell-v1`
Folder: `SUPERADMIN-PHASE1-ENTERPRISE-SHELL-V1`
Patch entrypoint: `apply_phase1.py`
Verification checklist: `VERIFY.md`

Target project: `/var/www/TCRMMT`

Instructions:
1. Before changing anything, inspect `git status` in `/var/www/TCRMMT` and report unrelated pre-existing changes. Do not discard, overwrite, stage, commit, or push them.
2. Fetch the exact patch branch/folder above into a temporary location outside the TCRMMT worktree.
3. Read `apply_phase1.py` and `VERIFY.md` before execution.
4. Run the patch script once. It must create its own backup of `server/_core/index.ts`.
5. This phase is strictly Design System + App Shell. Do not change authentication, database, API routes, permissions, tenant logic, billing logic, or business behavior.
6. Run the verification checklist. Build must succeed before restart.
7. Restart only the TCRMMT web application process if and only if the build succeeds. Do not restart DB, workers, or unrelated services.
8. Test Super Admin login and all existing navigation destinations. Owner-only items must remain owner-only.
9. Test sidebar expanded/collapsed state, light/dark theme, 1440x900 desktop, and one narrow/mobile viewport.
10. Capture screenshots for Overview, Companies, Users, one Integrations page, System Settings, and collapsed sidebar.
11. Do not commit or push TCRMMT. The final production Git push will be done manually by the owner from the system after approval.
12. Return a concise report: files changed, backup path, check/build result, restart result, login/navigation result, screenshots, and any regression found.

Expected visual direction: premium Enterprise SaaS control center, clean Navy foundation with restrained Tamiyouz Gold accent, neutral surfaces, clearer hierarchy, grouped navigation, lower visual density, and a consistent shell without redesigning page-specific business content yet.
