-- EASY
-- 19. Show the OrderID, OrderDate(date only) and CompanyName(Shippers) for all Orders 
-- with OrderID<10270. Sort by OrderID. (22 rows). Note: when you join two tables, the 
-- field that's joined on not necessarily need to have the same name - ShipVia in Orders 
-- and ShipperID in Shippers.
SELECT orders.orderid, DATE(orders.orderdate), shippers.companyname
FROM orders
JOIN shippers ON orders.shipvia = shippers.shipperid
WHERE orderid < 10270
ORDER BY orderid
;