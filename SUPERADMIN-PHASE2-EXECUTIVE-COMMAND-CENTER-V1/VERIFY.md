# TCRMMT Super Admin Phase 2 — Executive Command Center V1

## Scope
Presentation-only redesign of the existing Super Admin Overview / Command Center.

Preserves all existing IDs, data rendering, handlers, routes, APIs, permissions, auth, and database behavior.

## Apply
Run once from a temporary location outside the project worktree:

```bash
python3 apply_phase2.py
```

The script is marker-guarded and refuses unknown baselines.

## Required validation

```bash
cd /var/www/TCRMMT
git diff --check
npm run check
npm run build
```

Only if all pass, restart the TCRMMT web process.

## Browser checks
At desktop width, verify:
- Overview loads without console/runtime regression.
- First viewport reads as an executive dashboard, not a wall of equal cards.
- Smart insight cards are compact and aligned.
- Executive ribbon is compact and readable.
- Detailed KPI section remains expandable and all existing values render.
- Quick decisions form a compact command palette.
- Search, alerts, usage and security remain functional.
- Sidebar collapse/expand still works and persists.
- Light and Dark themes both work.
- No horizontal page overflow.

Also spot-check Companies, Users, GitHub Sync, Evolution API, Activity and Settings for shell regressions.

## Screenshots requested
- Overview expanded, above the fold
- Overview with KPI details expanded
- Overview dark mode
- Overview with collapsed sidebar

## Prohibited
- No DB changes
- No API changes
- No auth changes
- No route changes
- No permission changes
- No business-logic changes
- No Commit
- No Push
