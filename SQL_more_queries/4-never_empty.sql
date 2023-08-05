-- Task: Create the table "id_not_null" in the specified database

-- Use the specified database (provided as an argument to the mysql command)
USE `#DB_NAME#`;

-- Create the table "id_not_null" if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
