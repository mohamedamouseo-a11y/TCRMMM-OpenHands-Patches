# Phase 2.5 — Dashboard Grid & Readability Final Fix

## Scope
Presentation/structure-only corrective for Super Admin Overview support area.

## Required baseline
- Phase 2.4 structural dashboard marker present.
- `STRUCTURAL_DASHBOARD_V24` present exactly once.
- `STRUCTURAL_SUPPORT_V24` present exactly once.

## Structural goal
- Replace the single 12-column support grid with two independent vertical columns.
- Primary column: Attention then Usage.
- Secondary column: Search then Security.
- This prevents a short Search card from creating a large blank area and prevents Security from being forced full-width by legacy grid cascade.

## Must preserve exactly once
- `refreshAlertsBtn`
- `commandFilters`
- `commandAlerts`
- `superAlerts`
- `refreshUsageBtn`
- `usageOverview`
- `globalSearchBox`
- `globalSearchBtn`
- `globalSearchResults`
- `securityPanel`
- `loadSecurityBtn`
- `securityReview`

## Visual acceptance
Desktop:
- Two independent support columns.
- No large empty white area below Search.
- Security appears directly below Search, not full-width.
- Attention and Usage stack naturally in the other column.
- Typography is visibly larger/readable than Phase 2.4.
- KPI numbers and labels have stronger hierarchy.
- Sidebar/topbar text remains readable.
- No clipping.
- No horizontal page overflow.

Responsive:
- <=1080px support area becomes one column.
- <=1080px KPI cards become two columns.
- <=700px KPI cards become one column.

Regression:
- Companies
- Users
- GitHub Sync
- Evolution API
- Activity
- Settings
- Sidebar collapse/persistence
- Light/Dark theme

## Required commands
```bash
git diff --check
npm run check
npm run build
```

Restart only `tamiyouz-crm` after all checks pass.

Do not commit or push.
