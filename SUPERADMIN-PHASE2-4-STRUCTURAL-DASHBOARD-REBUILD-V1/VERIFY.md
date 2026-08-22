# Phase 2.4 — Structural Dashboard Rebuild V1

Target: `/var/www/TCRMMT/server/_core/index.ts`

## Scope
- Rebuild only the Super Admin Overview + Support HTML structure.
- Preserve all existing IDs used by data renderers and handlers.
- Add scoped CSS for the new structure.
- No DB/API/Auth/Routes/Permissions/Business Logic/Data Handler changes.

## Required baseline markers
- `SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1`
- `SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1`
- `SUPER_ADMIN_PHASE2_EXECUTIVE_COMMAND_CENTER_V1`
- `SUPER_ADMIN_PHASE2_1_RESPONSIVE_NO_CLIPPING_V1`
- `SUPER_ADMIN_PHASE2_2_FINAL_DASHBOARD_COMPOSITION_V1`
- `SUPER_ADMIN_PHASE2_3_VISUAL_REBUILD_V1`

## Preserved IDs — must remain exactly once
`smartInsights`, `executiveRibbon`, `commandDetails`, `operationsPulse`, `metrics`, `quickAddCompanyBtn`, `quickCreateTenantBtn`, `quickAuditBtn`, `quickSourceBtn`, `quickUsageReportBtn`, `quickNotifyBtn`, `commandFilters`, `commandAlerts`, `globalSearchBox`, `globalSearchBtn`, `globalSearchResults`, `refreshAlertsBtn`, `superAlerts`, `refreshUsageBtn`, `usageOverview`, `securityPanel`, `loadSecurityBtn`, `securityReview`.

## Verification
1. `git status --short`
2. Run patch once: `python3 apply_phase2_4.py`
3. Confirm marker `SUPER_ADMIN_PHASE2_4_STRUCTURAL_DASHBOARD_REBUILD_V1` exists exactly once as a block.
4. Confirm `STRUCTURAL_DASHBOARD_V24` and `STRUCTURAL_SUPPORT_V24` exist in the live Super Admin template.
5. Check each preserved ID occurs exactly once.
6. `git diff --check`
7. `npm run check`
8. `npm run build`
9. Restart only `tamiyouz-crm` after successful build.

## Browser acceptance
Desktop:
- Header is compact and not a decorative hero card.
- Four primary KPIs are readable with stronger number hierarchy.
- Executive row has 3 summary cards + KPI details panel, no decorative circles/blobs.
- Quick Commands panel is full-width and compact.
- Support grid is explicit and balanced: Attention 7/12, Search 5/12, Usage 6/12, Security 6/12.
- No artificial whitespace caused by equal-height grid rows.
- Search results and long lists use internal scroll only when needed.
- No clipping or horizontal page overflow.

Responsive:
- <=1180: 2 KPI columns, 3 quick-action columns, executive row stacks.
- <=900: support cards become single-column and executive ribbon stacks.
- <=640: primary KPIs and quick actions become single-column.

Regression spot checks:
- Companies
- Users
- GitHub Sync
- Evolution API
- Activity
- Settings
- Sidebar expand/collapse persistence
- Light/Dark

## Evidence requested
- `01-overview-above-fold.webp`
- `02-overview-full.webp`
- `03-kpi-details-open.webp`
- `04-dark-mode.webp`
- `05-sidebar-collapsed.webp`

Do not Commit or Push from Manus.