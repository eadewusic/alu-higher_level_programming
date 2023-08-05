-- Task: Create the table "unique_id" in the specified database

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- Create the table "unique_id" if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
);
