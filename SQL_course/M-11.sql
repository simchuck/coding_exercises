-- MEDIUM
-- 11. Show all Customers who have never placed an order with Employee 4.(16 rows)
SELECT DISTINCT customers.companyname, orders.employeeid
FROM customers
LEFT OUTER JOIN orders ON orders.customerid = customers.customerid
WHERE 
	NOT orders.employeeid = 4
ORDER BY customers.companyname
;
-- 2019.04.27
-- using SELECT DISTINCT with both companyname and employeeid treats all combinations as distinct