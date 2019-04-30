-- MEDIUM
-- 4. Incorporate UnitsInOrder and Discontinued fields. So, now UnitsInOrder + UnitsInStock 
-- <= ReorderLevel and  Discontinued flag is False. (2 rows)
SELECT productname, unitsinstock, reorderlevel, unitsinstock - reorderlevel AS buffer
FROM products
WHERE 
  UnitsOnOrder + UnitsInStock <= ReorderLevel 
AND  
  NOT Discontinued
ORDER BY buffer ASC
;