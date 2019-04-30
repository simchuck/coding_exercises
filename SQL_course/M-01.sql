-- MEDIUM
-- 1. Show the list with CategoryNames and the TotalNumber of products for each 
-- Category sorted by number of products in desc order. (8 rows). Here you have 
-- to combine JOIN and GROUP BY.
SELECT categories.categoryname, count(products) AS NumberOfProducts
FROM categories
JOIN products ON categories.categoryid = products.categoryid
GROUP BY categories.categoryname
ORDER BY NumberOfProducts DESC
;