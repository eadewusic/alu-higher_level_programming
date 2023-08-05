-- Task: Create the database "hbtn_0d_usa" and the table "states"
-- Step 1: Create the database "hbtn_0d_usa" if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Step 2: Use the database "hbtn_0d_usa"
-- USE hbtn_0d_usa;

-- Step 3: Create the table "states" if it does not exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
);
