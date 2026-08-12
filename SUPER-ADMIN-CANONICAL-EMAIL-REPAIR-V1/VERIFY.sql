-- TCRMMM SUPER ADMIN CANONICAL EMAIL REPAIR V1 VERIFY

SELECT COUNT(*) AS root_owner_count
FROM super_admins
WHERE is_active=1
  AND LOWER(TRIM(role))='owner'
  AND created_by_super_admin_id IS NULL;

SELECT id, email, role, is_active, created_by_super_admin_id, session_version
FROM super_admins
WHERE is_active=1
  AND LOWER(TRIM(role))='owner'
  AND created_by_super_admin_id IS NULL;

SELECT COUNT(*) AS old_email_count
FROM super_admins
WHERE LOWER(TRIM(email))='admin@tamiyouz.com';

SELECT COUNT(*) AS target_email_count
FROM super_admins
WHERE LOWER(TRIM(email))='superadmin@tamiyouzalrowad.com';

SELECT COUNT(*) AS reset_table_count
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA=DATABASE()
  AND TABLE_NAME='super_admin_password_reset_tokens';

SELECT COUNT(*) AS migration_history_count
FROM __master_schema_migrations
WHERE name='master-migration-super-admin-password-recovery-v1.sql';
