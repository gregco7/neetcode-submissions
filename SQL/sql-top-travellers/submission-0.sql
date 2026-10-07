-- Write your query below
SELECT u.name, COALESCE (SUM(r.distance),0) as travelled_distance
FROM users u
LEFT JOIN rides r on r.user_id = u.id
GROUP BY u.name  
ORDER BY 
    travelled_distance DESC,
    name ASC;

