-- Task: List all genres of the show "Dexter" from hbtn_0d_tvshows

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- List all genres of the show "Dexter"
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
