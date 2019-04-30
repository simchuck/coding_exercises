-- MEDIUM
-- 6. We want to investigate some more shipping options for our customers. Return 
-- the three countries with the highest average freight ordered by average freight 
-- in descending order. Use GROUP BY, AVE() and LIMIT statements
SELECT 
	shipcountry AS Country, AVG(freight::NUMERIC) AS AverageFreight
FROM orders
GROUP BY shipcountry
ORDER BY AverageFreight DESC
LIMIT 3
;