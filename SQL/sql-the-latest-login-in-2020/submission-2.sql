-- Write your query below

SELECT u.user_id, MAX(u.time_stamp) AS last_stamp
    FROM logins AS u
    WHERE u.time_stamp >= '2020-01-01' AND u.time_stamp < '2021-01-01'

GROUP BY u.user_id