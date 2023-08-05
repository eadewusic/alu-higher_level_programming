-- Task: List all cities of California from the hbtn_0d_usa database

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- List all cities of California without using the JOIN keyword
SELECT * 
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id;
