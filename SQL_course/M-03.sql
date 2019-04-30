-- MEDIUM
-- 3. What Products do we have in our inventory that needs to be reordered? Sort results 
-- by ProductID.  (22 rows). Use UnitsInStock field  <=  ReorderLevel field only
SELECT productname, unitsinstock, reorderlevel, unitsinstock - reorderlevel AS buffer
FROM products
WHERE unitsinstock <= reorderlevel
ORDER BY buffer ASC
;