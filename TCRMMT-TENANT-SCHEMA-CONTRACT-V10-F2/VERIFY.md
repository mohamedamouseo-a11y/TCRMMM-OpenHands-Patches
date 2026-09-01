# TCRMMT — Tenant Schema Contract V10 / Table Count 199 F2

## Purpose
Fix the proven provisioning contract mismatch that blocks new tenants with:

`tenant_schema_manifest_version_invalid:10:required=9`

Production evidence proved:
- tenant schema manifest: `schemaVersion=10`
- minimum compatible version: `10`
- manifest required table count: `199`
- provisioning contract still declared schema version `9`
- provisioning contract still declared final required table count `198`

Updating only version 9 -> 10 is insufficient because the next manifest validation would compare manifest table count 199 against contract table count 198. F2 aligns both contract constants with the existing manifest.

## Patch
Repository: `mohamedamouseo-a11y/TCRMMM-OpenHands-Patches`

Branch: `tenant-schema-contract-v10-f2`

Folder: `TCRMMT-TENANT-SCHEMA-CONTRACT-V10-F2`

Files:
- `apply_tcrmmm_tenant_schema_contract_v10_f2.py`
- `VERIFY.md`

Base patch head: `7a29c03fe455dcb387d37c46cd67a93a5d0decad`

Production target: `/var/www/TCRMMT`

Production branch remains `master`.

## Functional scope
F2 modifies only:

`/var/www/TCRMMT/scripts/provisioning-schema-contract.mjs`

Changes:
- `TENANT_SCHEMA_CURRENT_VERSION`: 9 -> 10
- `TENANT_SCHEMA_FINAL_REQUIRED_TABLES`: 198 -> 199
- derived `TENANT_SCHEMA_FINAL_PHYSICAL_TABLES` automatically becomes 201 because there are two schema system tables.

Marker:

`TCRMMT_TENANT_SCHEMA_CONTRACT_V10_TABLECOUNT_199_F2`

No bilingual runtime/version change.
No database mutation is performed by the patch itself.
No manual SQL reset is allowed.

## Preflight
Run from `/var/www/TCRMMT`:

- `git branch --show-current`
- `git status --short`
- `git rev-parse HEAD`

Branch must remain `master`.

Allowed cumulative tracked modified files after F2 are only:
- `server/_core/index.ts`
- `server/superAdminUiPolish.ts`
- `scripts/provisioning-schema-contract.mjs`

Any unexpected fourth tracked modified file: STOP.

Do not reset, clean, restore, commit, or push production.

Before apply verify current source still has exactly:
- `export const TENANT_SCHEMA_CURRENT_VERSION = 9;`
- `export const TENANT_SCHEMA_FINAL_REQUIRED_TABLES = 198;`

Verify existing manifest exactly reports:
- `schemaVersion = 10`
- `minimumCompatibleSchemaVersion = 10`
- `requiredTableCount = 199`

The patch script also enforces these manifest preconditions and must STOP if they differ.

## Apply twice
Run the official F2 patch script twice.

First exact output:

`Applied TCRMMT tenant schema contract V10/table-count 199 F2.`

Second exact output:

`TCRMMT tenant schema contract V10/table-count 199 F2 already applied; no changes made.`

Second run must be an exact no-op.

## Source verification
Confirm:
- marker exists
- `TENANT_SCHEMA_CURRENT_VERSION = 10`
- `TENANT_SCHEMA_FINAL_REQUIRED_TABLES = 199`
- `TENANT_SCHEMA_FINAL_PHYSICAL_TABLES` is still derived from final required tables + system tables

Run:
- `node --check scripts/provisioning-schema-contract.mjs`
- `node --check scripts/provisioning-worker.mjs`

Then load the contract and manifest read-only and verify `assertTenantSchemaFinalManifest(manifest)` succeeds.

Expected verified values:
- schema version 10
- minimum compatible version 10
- required tenant table count 199
- expected physical table count 201

## Project gates
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS.

If any gate fails: STOP. No manual fix and no restart.

## Worker restart
The provisioning worker imports `./provisioning-schema-contract.mjs` directly, so after all gates pass restart ONLY:

`tamiyouz-crm-provisioning-worker`

Restart it exactly ONCE.

Do NOT restart `tamiyouz-crm` for this F2 unless a new independent reason is proven.

Confirm worker is online and its new PM2 start time is after the F2 source change.

## Hamdi official recovery
Existing tenant:
- id: 17
- slug: `hamdi`
- current status before recovery: `provision_failed`
- current schema version before recovery: `0`
- old job id: 16, failed 3/3

After F2 + worker restart, use ONLY the official authenticated Super Admin retry route:

`POST /api/super-admin/tenants/17/retry-provisioning`

Retry exactly ONCE.

Do not use manual DB reset.
Do not delete provisioning jobs manually.
Do not change tenant status manually.
Do not create another tenant.
Do not bypass Super Admin authentication.

If an authenticated Super Admin session is not available to OpenHands, STOP after patch + worker verification and report `READY FOR AUTHENTICATED OFFICIAL RETRY: YES`; do not fabricate cookies/tokens.

## Monitor after official retry
If the official retry was successfully issued, monitor read-only until terminal state or a reasonable timeout.

Expected successful result:
- newest provisioning job: `done` / equivalent success
- tenant status: `trialing` or `active` according to requested state
- tenant schema version: `10`
- schema compatibility: YES
- maintenance gate no longer appears on tenant login

If the retry fails with any new error:
- STOP
- do not retry a second time
- capture exact sanitized error code/message
- do not manually fix

## Privacy
Do not expose:
- owner/admin email
- password/hash
- DB passwords
- credentials
- tokens
- cookies
- JWT/session values
- provisioning payload JSON

## Final classification
Report:

PATCH APPLY: PASS / FAIL
SECOND APPLY NO-OP: PASS / FAIL
MANIFEST PRECONDITION: PASS / FAIL
CONTRACT VERSION: 10 / OTHER
CONTRACT TABLE COUNT: 199 / OTHER
PHYSICAL TABLE COUNT EXPECTED: 201 / OTHER
CONTRACT-MANIFEST ASSERTION: PASS / FAIL
DIFF CHECK: PASS / FAIL
TYPE CHECK: PASS / FAIL
BUILD: PASS / FAIL
WORKER RESTART EXACTLY ONCE: PASS / FAIL
WORKER ONLINE: YES / NO
OFFICIAL RETRY ISSUED: YES / NO
OFFICIAL RETRY COUNT: 0 / 1
FINAL JOB STATUS: <status>
FINAL TENANT STATUS: <status>
FINAL TENANT SCHEMA VERSION: <number>
SCHEMA COMPATIBLE: YES / NO
HAMDI MAINTENANCE GATE: PRESENT / CLEARED / NOT TESTED
NEW BLOCKER: <exact sanitized error or NONE>
FUNCTIONAL PATCH REQUIRED: YES / NO

## Evidence
Create exactly:

`TCRMMT_TENANT_SCHEMA_CONTRACT_V10_F2_Evidence.zip`

Upload Final Report + Evidence ZIP into ChatGPT session exactly:

`TCRMMMT`

No production commit/push.
