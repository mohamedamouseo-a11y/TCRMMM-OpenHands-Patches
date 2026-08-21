# Super Admin Phase 1.1 — Visual Corrective Verification

Target: `/var/www/TCRMMT`

## Required checks

1. `git status --short`
2. Run `python3 apply_phase1_1.py`
3. `git diff --check`
4. `npm run check`
5. `npm run build`
6. Restart only the TCRMMT web process if build passes.
7. Browser verify:
   - `/super-admin#overview`
   - `/super-admin#tenants`
   - `/super-admin#users`
   - `/super-admin#github`
   - `/super-admin#evolution-api`
   - Settings drawer
   - sidebar expanded/collapsed
   - light/dark
8. Desktop screenshot at 1440x900 or wider, especially GitHub Sync.
9. Verify content area is not squeezed by sidebar and no horizontal page overflow exists.
10. Do not commit or push.

## Scope guard

This patch is visual-only. It must not change APIs, DB, auth, routes, permissions, secrets, business logic, or production data.
