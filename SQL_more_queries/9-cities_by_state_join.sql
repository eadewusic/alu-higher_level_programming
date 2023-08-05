-- Task: List all cities and their corresponding state names from the hbtn_0d_usa database

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- List all cities and their corresponding state names
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
