-- EASY
-- 16.  Get a list of all unique ContactTitles from Customers table. Use Distinct or Group By 
SELECT DISTINCT contacttitle
FROM customers
;

SELECT contacttitle
FROM CUSTOMERS
GROUP BY contacttitle
;