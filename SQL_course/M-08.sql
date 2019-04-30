-- MEDIUM
-- 8. Return the same result as previous problem, but for last 12 months only.
-- NOTE: Most recent data in this database is from 2016
--		SELECT (NOW() - INTERVAL '1 YEAR')  AS OneYearAgo;	=>	2018-04-26 22:13:41.159519+00
--		SELECT MAX(orderdate) FROM orders;					=> 	2016-05-06 18:00:00
SELECT 
	shipcountry AS Country, max(orderdate), AVG(freight::NUMERIC) AS AverageFreight
FROM orders
WHERE (orderdate >= (NOW() - INTERVAL '1 YEAR'))
GROUP BY shipcountry
ORDER BY AverageFreight DESC
LIMIT 3
;