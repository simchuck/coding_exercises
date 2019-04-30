-- EASY
-- 8. Show OrderID, CustomerID and ShipCountry for Orders shipping to France or Belgium. (96 rows)
SELECT orderid, customerid, shipcountry
FROM orders
WHERE shipcountry = 'France' OR shipcountry = 'Belgium'
;