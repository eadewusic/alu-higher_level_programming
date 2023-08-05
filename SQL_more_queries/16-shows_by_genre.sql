-- Task: List all shows and their linked genres (or NULL) from hbtn_0d_tvshows

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- List all shows and their linked genres (or NULL)
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
