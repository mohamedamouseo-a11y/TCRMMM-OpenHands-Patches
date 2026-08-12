-- TCRMMM SUPER ADMIN CANONICAL EMAIL REPAIR V1
-- Master DB only.
-- Preconditions must be checked by the operator before running this transaction.
-- Expected current root owner: admin@tamiyouz.com
-- Required canonical root owner: superadmin@tamiyouzalrowad.com

START TRANSACTION;

SELECT id, email, role, is_active, created_by_super_admin_id, session_version
FROM super_admins
WHERE is_active=1
  AND LOWER(TRIM(role))='owner'
  AND created_by_super_admin_id IS NULL
FOR UPDATE;

SELECT id
FROM super_admins
WHERE LOWER(TRIM(email))='superadmin@tamiyouzalrowad.com'
FOR UPDATE;

UPDATE super_admins
SET email='superadmin@tamiyouzalrowad.com',
    session_version=COALESCE(session_version,0)+1,
    updated_at=NOW()
WHERE LOWER(TRIM(email))='admin@tamiyouz.com'
  AND is_active=1
  AND LOWER(TRIM(role))='owner'
  AND created_by_super_admin_id IS NULL;

-- Operator MUST confirm ROW_COUNT() = 1 before COMMIT.
SELECT ROW_COUNT() AS rows_updated;

COMMIT;
