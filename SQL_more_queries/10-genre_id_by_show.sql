-- Task: List all shows from hbtn_0d_tvshows that have at least one genre linked

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- List all shows with at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
