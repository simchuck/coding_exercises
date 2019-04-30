-- EASY
-- 9. Select OrderID, CustomerID and ShipCountry for Orders shipping to Brazil, Mexico, 
-- Argentina, Venezuela (Latin America). (173 rows). Use 'in' instead of multiple OR)
SELECT orderid, customerid, shipcountry
FROM orders
WHERE shipcountry IN ('Brazil', 'Mexico', 'Argentina', 'Venezuela')
;