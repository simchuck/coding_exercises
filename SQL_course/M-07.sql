-- MEDIUM
-- 7.Return the same result as previous problem, but for only 2015. You can use BETWEEN 
-- statement. France should be the third country.
SELECT 
	shipcountry AS Country, AVG(freight::NUMERIC) AS AverageFreight
FROM orders
WHERE EXTRACT(YEAR FROM orderdate) = 2015
GROUP BY shipcountry
ORDER BY AverageFreight DESC
LIMIT 3
;