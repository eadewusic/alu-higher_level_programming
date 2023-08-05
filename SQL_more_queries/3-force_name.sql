-- Task: Create the table "force_name" in the specified database

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- Create the table "force_name" if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
    PRIMARY KEY (id)
);
