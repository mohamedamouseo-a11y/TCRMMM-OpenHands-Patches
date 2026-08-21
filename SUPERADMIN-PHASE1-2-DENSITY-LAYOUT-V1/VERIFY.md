# TCRMMT Super Admin Phase 1.2 — Verify

Target: `/var/www/TCRMMT`

## Preconditions
- Do not clean/reset/restore the worktree.
- Phase 1.1 marker must already exist in `server/_core/index.ts`.
- This patch is presentation-only CSS.

## Apply
```bash
cd /var/www/TCRMMT
python3 /path/to/apply_phase1_2.py
```

## Required checks
```bash
git diff --check
npm run check
npm run build
```

Only if build passes, restart the TCRMMT web process only.

## Visual checks
Validate at desktop width (preferably 1440×900 or larger):
- `#activity`: cards are compact and use 2 columns on wide desktop; no large empty white rows.
- Topbar is one compact row on desktop with identity, search, and actions aligned.
- Sidebar is narrower/denser without clipped labels or controls.
- Main content is centered with efficient width and no page-level horizontal overflow.
- `#github`: status cards and workspace remain readable and not squeezed.
- Collapsed sidebar still works and persists.
- Light and dark themes still work.

Also test Overview, Companies, Users, Evolution API, Settings, Activity and GitHub Sync.

## Safety
Do not change DB, APIs, routes, auth, permissions or business logic. Do not commit or push.

## Evidence
Return screenshots for Activity, GitHub Sync, Overview, and collapsed sidebar plus a short validation report.
