# TCRMMT Functional F2 — Tenant Provisioning Schema Contract V10

## Purpose

Repair the confirmed provisioning contract mismatch that rejects the production tenant-migration manifest before migrations can run.

Confirmed mismatch:

- source contract: `TENANT_SCHEMA_CURRENT_VERSION = 9`
- production manifest evidence: `schemaVersion = 10`
- failure: `tenant_schema_manifest_version_invalid:10:required=9`

This is a **functional-only** patch. It is unrelated to the Super Admin bilingual runtime patch chain.

## Scope

The F2 patch may modify exactly one project file:

`/var/www/TCRMMT/scripts/provisioning-schema-contract.mjs`

Exact source replacement:

```diff
-export const TENANT_SCHEMA_CURRENT_VERSION = 9;
+export const TENANT_SCHEMA_CURRENT_VERSION = 10;
```

No database edits are part of this patch.

## Production preflight — mandatory

Before applying the patch:

1. Confirm project root is `/var/www/TCRMMT` and branch is `master`.
2. Record current main-repo HEAD and `git status --short` without modifying or cleaning anything.
3. Confirm `scripts/provisioning-schema-contract.mjs` contains exactly one old v9 contract line and no v10 contract line.
4. Confirm `/var/www/TCRMMT/scripts/tenant-migrations/manifest.json` exists in production and its `schemaVersion` is exactly `10`.
5. Confirm Hamdi tenant id `17` remains failed/incompatible and no retry has been run during this recovery attempt.
6. Preserve all pre-existing dirty files. Do not reset, clean, restore, checkout, stash, or overwrite unrelated work.

If the production manifest is missing or is not `schemaVersion=10`, **STOP** and collect evidence. Do not apply this F2 patch.

## Apply

Run the official patch script from the patch package against `/var/www/TCRMMT`.

First application must print exactly:

`Applied F2 tenant provisioning schema contract v10 fix.`

Second application must print exactly:

`F2 tenant provisioning schema contract v10 fix already applied; no changes made.`

The second run must be an exact no-op.

After application, verify the F2 delta is only the one-line contract change from 9 to 10. Any additional file modified by F2 is a STOP condition. Pre-existing unrelated dirty files must remain untouched.

## Gates

Run:

```bash
git diff --check
npm run check
npm run build
```

All must pass.

Then verify:

- source contract resolves to required version `10`;
- newly built provisioning runtime resolves to required version `10`;
- production manifest remains version `10`.

Do not continue if source/build/manifest do not all agree on version 10.

## Worker activation

After all gates pass, restart **only**:

`tamiyouz-crm-provisioning-worker`

Restart it exactly once. Do not restart the main `tamiyouz-crm` process for this F2 recovery.

Capture worker restart count/start epoch before and after and verify the new worker instance is running the rebuilt contract. Confirm the old error `tenant_schema_manifest_version_invalid:10:required=9` is not emitted by the new worker startup/runtime.

## Official retry — exactly once

Only after the patch, build validation, and worker restart succeed, invoke the authenticated official route exactly once as SuperAdmin owner/admin:

`POST /api/super-admin/tenants/17/retry-provisioning`

Do not manually update `tenants`, delete provisioning jobs, or use any database fallback.

Monitor the resulting job to terminal state for up to approximately 180 seconds.

If the retry fails, **STOP**. Do not issue a second retry. Capture the exact new error, job id/status/attempts, tenant status, and tenant schema version.

## Success criteria

A successful recovery must demonstrate all of the following:

- official retry count during recovery: exactly 1;
- provisioning job reaches its normal successful/completed state;
- Hamdi tenant reaches the application's normal healthy/active provisioned state;
- tenant `schema_version = 10`;
- schema compatibility = YES;
- Hamdi login maintenance gate is cleared;
- no manual DB changes were made;
- no production commit or push was made.

## Evidence

Create:

`TCRMMT_HAMDI_PROVISIONING_SCHEMA_V10_F2_Evidence.zip`

Include a final report with at least:

- main repo HEAD before apply;
- pre-existing `git status --short`;
- source required version pre/post;
- production manifest version;
- built/runtime required version pre/post;
- exact first/second patch outputs;
- `git diff --check`, `npm run check`, `npm run build` results;
- worker restart count and start epoch before/after;
- worker restart count during recovery;
- official retry count;
- resulting job id/status/attempts;
- final tenant status;
- final tenant schema version;
- schema compatibility;
- login maintenance gate state;
- any new provisioning error, if present;
- confirmation: manual DB changes = NO;
- confirmation: production commit/push = NO.

Upload the final report and Evidence ZIP to ChatGPT session exactly: `TCRMMMT`.
