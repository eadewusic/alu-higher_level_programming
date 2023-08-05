-- Task: Create the MySQL server user "user_0d_1" with privileges and set password

-- Step 1: Create the user "user_0d_1" if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Step 2: Grant all privileges to the user "user_0d_1" on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Step 3: Revoke specific privileges from the user "user_0d_1"
-- (Optional: Only if certain privileges need to be revoked)
REVOKE AUDIT_ABORT_EXEMPT, FIREWALL_EXEMPT, AUTHENTICATION_POLICY_ADMIN, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN ON *.* FROM 'user_0d_1'@'localhost';
