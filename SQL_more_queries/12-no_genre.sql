-- Task: List all shows from hbtn_0d_tvshows without a genre linked

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- List all shows without a genre linked
SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tvsg
ON tvs.id = tvsg.show_id
WHERE tvsg.genre_id IS NULL
ORDER BY tvs.title, tvsg.genre_id;
