-- Task: List all Comedy shows from hbtn_0d_tvshows

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- List all Comedy shows
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
