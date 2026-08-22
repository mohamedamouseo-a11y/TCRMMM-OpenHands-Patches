# Phase 2.2 — Final Dashboard Composition V1

Target: `/var/www/TCRMMT`

## Scope
Presentation-only composition correction for Super Admin Overview. No DB/API/Auth/Routes/Permissions/Business Logic/Data Handler changes.

## Baseline requirements
The target source must already contain these markers:
- `SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1`
- `SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1`
- `SUPER_ADMIN_PHASE2_EXECUTIVE_COMMAND_CENTER_V1`
- `SUPER_ADMIN_PHASE2_1_RESPONSIVE_NO_CLIPPING_V1`

## Required validation
Run in this order:

```bash
git status --short
python3 /tmp/apply_phase2_2.py
git diff --check
npm run check
npm run build
```

Restart only `tamiyouz-crm` after all checks pass.

## Visual acceptance criteria

### Overview desktop
- No giant white gaps between Search / Alerts / Usage / Security panels.
- Quick Actions is full-width and compact.
- Four Smart Insights remain visible as one clean row when desktop space allows.
- Executive Ribbon remains 3 columns on desktop.
- Support deck naturally fills two vertical columns without equal-row-height artifacts.
- Search card uses only the height its content needs.
- Alerts / Usage / Security lists use bounded internal scroll when long.
- No text, badge, button, card, or list clipping.
- No horizontal page overflow.

### Responsive
- <=1260px: Quick Actions becomes 3 columns.
- <=980px: support deck becomes one column; Smart Insights and KPI metrics become 2 columns.
- <=700px: Smart Insights, Ribbon, KPIs, Quick Actions and Command Alerts become one column.

### Regression spot checks
Confirm these still render and navigate correctly:
- Companies
- Users
- GitHub Sync
- Evolution API
- Activity
- Settings
- Sidebar collapse / persistence
- Light / Dark theme

## Screenshots required
1. Overview desktop above fold.
2. Overview full support deck showing no giant gaps.
3. KPI Details open.
4. Overview dark.
5. Sidebar collapsed.

## Safety
- Do not Reset/Clean/Restore pre-existing changes.
- Do not Commit or Push.
- Do not modify database or production data.
- Do not run GitHub Sync/Push/Pull/Cleanup actions during visual verification.
