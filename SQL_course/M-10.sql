-- MEDIUM
-- 10. Show all "customers" you have never placed an order.(2 rows). You can use LEFT JOIN
SELECT customers.companyname
FROM customers
LEFT OUTER JOIN orders ON orders.customerid = customers.customerid
WHERE orders.orderid IS NULL
;