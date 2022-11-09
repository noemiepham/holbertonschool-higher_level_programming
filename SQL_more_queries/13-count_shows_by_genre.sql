-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)

-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tg.`name` AS `genre`,
      COUNT(*) AS `number_of_shows`
   FROM `tv_genres` AS tg
   INNER JOIN `tv_show_genres` AS tvg
   ON tg.id = tvg.genre_id
GROUP BY tg.name
ORDER BY number_of_shows DESC;
