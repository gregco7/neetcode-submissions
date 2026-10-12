-- Write your query below
-- product_id : volume query
SELECT w.name AS warehouse_name, SUM (
    w.units * p.length * p.width * p.height
) AS volume

FROM warehouse as w
LEFT JOIN 
    products as p on w.product_id = p.product_id

GROUP BY w.name

