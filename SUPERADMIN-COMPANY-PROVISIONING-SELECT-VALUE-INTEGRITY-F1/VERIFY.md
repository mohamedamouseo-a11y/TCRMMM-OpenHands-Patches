# TCRMMT Super Admin — Company Provisioning Select Value Integrity F1

## Purpose
Fix `Create New Company` returning `invalid_plan` after bilingual UI translation changes visible `<option>` text. The original Plan and Status options have no explicit `value`, so translating `starter` / `trialing` also changes the submitted select value. This patch preserves canonical machine values with explicit `value` attributes while allowing visible labels to be translated normally.

## Scope
Functional-only. No bilingual runtime/version bump.

Target file only:
- `/var/www/TCRMMT/server/_core/index.ts`

Marker:
- `SUPER_ADMIN_COMPANY_PROVISIONING_SELECT_VALUE_INTEGRITY_F1`

Changes:
- Add explicit `value="starter|pro|enterprise"` to initial Create Company plan options.
- Add explicit `value="trialing|active"` to initial Create Company status options.
- Dynamic `planOptions()` now emits explicit canonical plan slug values.
- Dynamic `statusOptions()` now emits explicit canonical status values.
- Visible option text remains available to the bilingual runtime for translation.
- No API contract, database logic, provisioning worker, plan registry, or business logic changes.

## Preconditions
- Production directory: `/var/www/TCRMMT`
- Production branch stays `master`.
- Existing cumulative modified tracked files may include `server/_core/index.ts` and `server/superAdminUiPolish.ts`.
- No reset / clean / restore.
- No manual edits.

## Apply
Run the official patch twice.

First exact output:
`Applied Super Admin company provisioning select-value integrity F1.`

Second exact output:
`Super Admin company provisioning select-value integrity F1 already applied; no changes made.`

## Gates
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must pass before restart.

## Restart
Restart only `tamiyouz-crm` exactly once after all gates pass. Confirm port 3002 becomes ready within 90 seconds and PM2 start epoch is newer than `dist/index.js` mtime.

## Browser QA
Fresh authenticated Super Admin browser; cache disabled.

Open Create New Company and inspect DOM before submit:
- `#newPlan` may display translated Arabic text, but its selected `.value` must be a canonical plan slug from `/api/super-admin/plans` (for example `starter`, not Arabic display text).
- `#newStatus` may display translated Arabic text, but its selected `.value` must be canonical (`trialing` or `active`).

Do not expose company/email/password values in evidence.

If the user's intended creation is retried, submit once only. Expected: request must not fail with `invalid_plan` or `invalid_status`. Stop and capture any new distinct error without manual fixing.

No production commit/push.
