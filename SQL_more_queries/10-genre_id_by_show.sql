-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT ts.`title`, tsg.`genre_id`
FROM `tv_shows` AS ts
     INNER JOIN `tv_show_genres` AS tsg 
     ON tsg.`show_id` = ts.`id`
ORDER BY ts.`title` ASC, tsg.`genre_id`  ASC;