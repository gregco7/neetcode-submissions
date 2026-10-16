SELECT ROUND ((100 * (SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1.0 ELSE 0.0 END) / COUNT(*))) ,2) as immediate_percentage
FROM delivery