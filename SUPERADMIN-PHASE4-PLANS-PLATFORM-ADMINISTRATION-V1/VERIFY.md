# Phase 4 — Plans & Platform Administration V1

## Scope

This patch changes presentation/structure only for:

1. `/super-admin` → `sec-platform-admins`
2. `/super-admin/plans`

It must not change DB, API, authentication, authorization, permissions, routes, business logic, data handlers, billing logic, plan semantics, subscription semantics, or GitHub sync behavior.

## Expected changed files

- `server/_core/index.ts`
- `server/superAdminPlansPage.ts`

No other project file should be modified by this patch.

## Platform Administration preserved IDs

Each of the following must exist exactly once after patching:

- `platformAdminsCount`
- `openPlatformAdminCreateBtn`
- `platformAdminStats`
- `platformAdminsBody`

Also verify the existing Platform Admin drawer still opens and saves through the current handlers.

## Plans workspace acceptance

Verify all three existing tabs still work without changing their behavior:

- Plans catalog
- Companies / overrides
- Commercial / subscriptions / billing

Verify existing forms, feature/limit editors, pricing, add-ons, commercial settings, subscriptions, rollout controls, invoice generation and tenant selection remain functional and unchanged logically.

## Visual acceptance

### Platform Administration

- Clear page header and Owner Only state.
- Stats are readable and compact.
- Admin table is inside a clean data card.
- Sticky table header.
- Actions are compact and readable.
- Drawer remains usable.
- No clipping or page-level horizontal overflow.
- Light/Dark both readable.

### Plans & Commercial

- Header is compact and no longer visually oversized.
- Three tabs are compact and clearly active/inactive.
- No decorative oversized gradients/cards dominating the page.
- Plans list/editor remain easy to scan.
- Feature and limit editors are denser but readable.
- Commercial view is usable without excessive whitespace.
- Sticky footer actions do not cover content.
- Responsive layout remains usable.
- No clipping or page-level horizontal overflow.

## Required commands

```bash
git diff --check
npm run check
npm run build
```

All must PASS before restart.

Restart only `tamiyouz-crm` after successful build.

## Regression spot checks

Check:

- Overview
- Companies
- Users
- Activity
- Audit
- GitHub Sync
- Evolution API
- Settings
- Sidebar collapse/persistence
- Light/Dark

## Screenshots required

1. Platform Admins above fold
2. Platform Admins table
3. Plans catalog above fold
4. Plans editor
5. Commercial view
6. Plans page narrow/responsive if the browser supports real viewport resizing

Do not Commit or Push.