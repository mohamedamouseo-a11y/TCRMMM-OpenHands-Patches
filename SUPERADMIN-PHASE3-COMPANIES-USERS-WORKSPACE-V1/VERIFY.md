# Phase 3 — Companies & Users Workspace V1 — Verification

Target: `/var/www/TCRMMT`

## Required baseline

- `SUPER_ADMIN_PHASE2_5_GRID_READABILITY_FINAL_FIX_V1`
- `STRUCTURAL_DASHBOARD_V24`

## Scope

Allowed:
- Replace the HTML structure of `#sec-tenants` and `#sec-users` only.
- Add scoped presentation CSS for Companies / Users workspace.

Forbidden:
- DB changes
- API changes
- Auth changes
- Route changes
- Permission changes
- Business logic changes
- Data handler changes
- Commit / Push

## Preserved IDs — must exist exactly once after patch

### Companies
- `tenantsCount`
- `currentTenantBadge`
- `tenantViewSummary`
- `savedFilters`
- `tenantSearch`
- `tenantStatus`
- `tenantPlan`
- `applyFiltersBtn`
- `createdFrom`
- `createdTo`
- `tenantPageSize`
- `resetFiltersBtn`
- `saveCurrentViewBtn`
- `exportTenantsBtn`
- `toggleDensityBtn`
- `densityIcon`
- `densityLabel`
- `tenantsBody`
- `tenantPager`

### Users
- `platformUsersCount`
- `platformUsersStats`
- `platformUserSearch`
- `platformUserTenant`
- `platformUserRole`
- `platformUserStatus`
- `loadPlatformUsersBtn`
- `platformUsersBody`
- `platformUsersPager`

## Commands

Run:

```bash
git status --short
python3 /path/to/apply_phase3.py
git diff --check
npm run check
npm run build
```

Only after all checks pass:

```bash
pm2 restart tamiyouz-crm --update-env
```

## Visual acceptance — Companies

- Header is clean and separate from data controls.
- Summary metrics render in 4 cards on desktop, 2 on medium, 1 on narrow.
- Search/filter block is visually distinct from the table.
- Search input has priority and is not cramped.
- Status + plan filters are readable.
- Secondary date/export/density controls are less visually dominant.
- Table header is sticky inside the table scroll container.
- Table rows are readable and actions are compact.
- No clipping.
- No page-level horizontal overflow.
- Existing company actions still work.

## Visual acceptance — Users

- Clean page header with summary metrics.
- Search/filter block uses clear hierarchy.
- User search has priority.
- Company / role / status selectors are readable.
- Users table is contained in one clean data card.
- Table header is sticky.
- User actions still work.
- No clipping or page-level horizontal overflow.

## Regression spot checks

- Overview
- Platform Admins
- Activity
- GitHub Sync
- Evolution API
- Settings
- Light / Dark
- Sidebar collapse / persistence

## Screenshots requested

1. Companies — above fold
2. Companies — table + filters
3. Users — above fold
4. Users — table + filters
5. Dark mode — Companies or Users
6. Sidebar collapsed — Companies or Users

Stop after report and screenshots. Do not commit or push.
