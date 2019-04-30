-- EASY
-- 6. Show SupplierID, ContactName and ContactTitle from Suppliers table where ContactTitle 
-- is not(!) Marketing Manager. (24 rows)
SELECT supplierID, contactname, contacttitle
FROM suppliers
WHERE NOT contacttitle = 'Marketing Manager'
;