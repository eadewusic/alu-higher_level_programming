-- Task: List all shows from hbtn_0d_tvshows that have at least one genre linked

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- List all shows with at least one genre linked
SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
INNER JOIN tv_show_genres AS tvsg
ON tvsg.show_id = tvs.id
ORDER BY tvs.title, tvsg.genre_id;
