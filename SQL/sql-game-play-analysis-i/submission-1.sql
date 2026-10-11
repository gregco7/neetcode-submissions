-- Write your query below

SELECT a.player_id, MIN(a.event_date) AS first_login
FROM activity AS a
GROUP BY a.player_id
ORDER BY a.player_id ASC