-- Task: Create the database "hbtn_0d_2" and the user "user_0d_2" with SELECT privilege

-- Step 1: Create the database "hbtn_0d_2" if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Step 2: Create the user "user_0d_2" if it does not exist and set the password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Step 3: Grant SELECT privilege to the user "user_0d_2" on the database "hbtn_0d_2"
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
