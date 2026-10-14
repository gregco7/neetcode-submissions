-- Write your query below
SELECT i.event_day AS day, i.emp_id, SUM (i.out_time - i.in_time) AS total_time
FROM employees AS i
GROUP BY i.event_day, i.emp_id;

