-- MEDIUM
-- 2. In the Customers table, show the total number of Customers per Country and City. (69 rows)
SELECT customers.country, customers.city, count(customers) AS TotalCustomers
FROM customers 
GROUP BY customers.country, customers.city
ORDER BY TotalCustomers DESC
;