-- Write your query below
-- Write a query to find salespeople who have never made sales to a specific company

SELECT s.name FROM sales_person AS s
WHERE s.sales_id NOT IN (
    SELECT o.sales_id FROM orders as o
    WHERE o.com_id IN (
        SELECT c.com_id FROM company as c
        WHERE c.name = 'CRIMSON')
)


