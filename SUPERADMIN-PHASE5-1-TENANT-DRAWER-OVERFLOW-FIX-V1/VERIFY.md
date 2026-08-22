# Phase 5.1 — Tenant Drawer Overflow Fix V1

## Scope

Fix only the dormant `#tenantDrawer` horizontal overflow found after Phase 5 validation.

The patch must not change DB, APIs, auth, routes, permissions, business logic, data handlers, drawer JavaScript, or any other Super Admin layout.

## Target

`/var/www/TCRMMT/server/_core/index.ts`

## Apply

Run exactly once:

```bash
python3 apply_phase5_1.py
```

The script is idempotent and must refuse an unknown baseline if the Phase 5 marker is missing.

## Required checks

```bash
git diff --check
npm run check
npm run build
```

All must PASS before restart.

## Runtime verification

After successful build, restart only the TCRMMT web process (`tamiyouz-crm`).

### Closed drawer acceptance

On a Super Admin page with `#tenantDrawer` closed:

1. Confirm the element has `aria-hidden="true"`, is not `.open`, and computed `display` is `none`.
2. Confirm page-level horizontal overflow is zero:
   - `document.documentElement.scrollWidth <= document.documentElement.clientWidth`
   - `document.body.scrollWidth <= document.body.clientWidth`
3. Confirm the previous ~10px overflow is gone.

### Open drawer acceptance

Open an existing company/tenant drawer and confirm:

1. Drawer becomes visible normally.
2. `aria-hidden="false"` and `.open` are present.
3. Tenant details load normally.
4. Tabs, buttons, close action, backdrop, ESC close, and focus behavior still work.
5. Closing the drawer returns computed `display:none` and zero page-level horizontal overflow.

### Regression spot check

- Activity
- Audit Log
- GitHub Sync
- Evolution API
- Tara APIs
- Companies
- Users
- Overview
- Light/Dark
- Sidebar collapse/persistence

## Evidence

Capture:

1. Closed tenant drawer + console measurements showing zero overflow.
2. Open tenant drawer rendering correctly.
3. One Phase 5 integration screen confirming no visual regression.

## Prohibited

- No Reset / Clean / Restore.
- No manual code edits beyond this patch.
- No Commit.
- No Push.
- No DB/API/Auth/Route/Permission/Business Logic changes.
