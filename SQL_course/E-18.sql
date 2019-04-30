-- EASY
-- 18. Show ProductID(Products), SupplierID(Suppliers,Products) and CompanyName(Suppliers) 
-- for each product from Products. (77 rows). This question introduces a new concept - 
-- INNER JOIN.
SELECT products.productid, suppliers.supplierid, suppliers.companyname
FROM products
INNER JOIN suppliers
  ON suppliers.supplierid::INT = products.supplierid::INT
;