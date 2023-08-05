-- Task: List all shows from hbtn_0d_tvshows
-- with their corresponding genre IDs (or NULL)

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- List all shows and their corresponding genre IDs (or NULL if they don't have a genre)
SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tvsg
ON tvs.id = tvsg.show_id
ORDER BY tvs.title, tvsg.genre_id;
