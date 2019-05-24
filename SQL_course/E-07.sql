-- 7. Show ProductID and ProductName from Products table where the ProductName 
-- includes 'queso'. (2 rows)
SELECT productid, productname
FROM products
WHERE LOWER(productname) LIKE '%queso%'
;