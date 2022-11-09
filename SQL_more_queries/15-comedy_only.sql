-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)
-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title

SELECT title
FROM tv_shows ts 
INNER JOIN tv_show_genres tsg ON (tsg.show_id = ts.id)
INNER JOIN tv_genres tg ON (tg.id = tsg.genre_id)
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;