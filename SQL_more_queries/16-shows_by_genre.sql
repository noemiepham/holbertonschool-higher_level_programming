-- write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
SELECT ts.title,tg.name
FROM tv_shows AS ts
     LEFT JOIN tv_show_genres AS tsg ON (tsg.show_id = ts.id)

     LEFT JOIN tv_genres AS tg ON (tsg.genre_id = tg.id)
ORDER BY ts.title ASC;