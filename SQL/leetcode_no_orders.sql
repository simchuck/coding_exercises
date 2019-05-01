# https://leetcode.com/problems/customers-who-never-order/

SELECT c.name AS Customers
FROM customers AS c
LEFT OUTER JOIN orders AS o
  ON c.id = o.customerid
  WHERE o.id IS NULL
;

