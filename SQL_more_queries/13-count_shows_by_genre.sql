-- Task: List all genres from hbtn_0d_tvshows and
-- the number of shows linked to each

-- Use the specified database (provided as an argument to the mysql command)
-- USE `#DB_NAME#`;

-- List all genres and the number of shows linked to each genre
SELECT genres.name AS genre, COUNT(tvsg.show_id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres AS tvsg
ON genres.id = tvsg.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
