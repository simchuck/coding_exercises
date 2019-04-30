-- MEDIUM
-- 9. Show OrderId, Quantity, ProductName, EmployeeID and LastName for each order in 
-- Orders table. Sort by OrderId and ProductID.(2155 rows). Yes, you have to JOIN 4 
-- tables and select only these columns.
SELECT 
	orders.OrderId, 
	orderdetails.Quantity, 
	products.ProductName, 
	orders.EmployeeID, 
	employees.LastName
FROM orders
JOIN orderdetails ON orders.OrderId = orderdetails.OrderId
JOIN employees ON orders.EmployeeId = employees.EmployeeId
JOIN products ON orderdetails.ProductID = products.ProductId
ORDER BY orders.OrderId, products.ProductId
;