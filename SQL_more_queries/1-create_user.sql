-- Task: Create MySQL server user "user_0d_1" with all privileges

-- Create the user "user_0d_1" with the specified password (if not exists)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user "user_0d_1" on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
