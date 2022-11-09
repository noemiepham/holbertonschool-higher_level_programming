-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)
-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
SELECT tg.`name`AS `name`
     FROM  tv_genres AS tg
          INNER JOIN tv_show_genres AS tsg
          ON tg.id = tsg.genre_id

          INNER JOIN tv_shows AS ts
          ON ts.id = tsg.show_id
          WHERE ts.title = "Dexter"
     ORDER BY tg.name ASC;

          






