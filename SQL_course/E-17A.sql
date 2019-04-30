-- EASY
-- 17. Get a NumberOfCustomers for each Country where we have Customers. Order 
-- it by NumberOfCustomers in DESC order.(21 rows). Use Group By clause.

-- variation: include WHERE clause to filter results

SELECT country, COUNT(1) AS NumberOfCustomers
FROM customers
WHERE LENGTH(city) < 6
GROUP BY country
ORDER BY NumberOfCustomers DESC
;