-- HARD
-- 1. Assuming that now is January 1, 2017, we want to find all high-value customers 
-- from 2016, who've made a least one order with a total value of $10,000 and give 
-- them VIP status. (6 rows)
WITH ordervalues AS (
	SELECT
		orders.customerid,
		orders.orderid,
		SUM(orderdetails.unitprice * orderdetails.quantity) AS ordervalue
	FROM orders
	JOIN orderdetails
		ON orderdetails.orderid = orders.orderid
	WHERE YEAR(orders.orderdate) IN (2017)
	GROUP BY orders.customerid, orders.orderid
	)
SELECT ordervalues.customerid AS VIPcustomer
FROM ordervalues
WHERE ordervalue > 10000::MONEY
ORDER BY ordervalue DESC
    
;
-- HARD
-- 2. What if sales person changes her mind and instead of 1 order with >$10,000 
-- would ask about $15,000 in total during 2016?
SELECT
FROM

;
-- HARD
-- 3. Change the above query including Discount in your calculations.  Order it 
-- by total amount which includes discount.
SELECT
FROM

ORDER totalvaluewithdiscount DESC

;
-- HARD
-- 4. At the end of the month salespeople are trying harder to get orders. Select 
-- all orders which were placed on the last dat of the month. Ordered by EmployeeID 
-- and OrderID. (24 rows)
SELECT
FROM

ORDER BY employeeid, orderid

;
-- HARD
-- 5. We want to identify the size of the table for our website. Show the top 10 
-- orders with maximum items. Ordered by number of items.
SELECT
FROM

ORDER BY totalitems DESC
LIMIT 10

;
-- HARD
-- 6. Select 2% of OrderDetails table. (41 rows). Use statement  random() < 0.02
SELECT
FROM

;
-- HARD
-- 7. One of the salespeople think that she accidentally entered line item twice 
-- on an order, each time with different ProductId, but the same quantity.  She 
-- remembers that quantity was 60 or more. Show all OrderID that match this, ordered 
-- by OrderID. (5 rows)
SELECT
FROM

ORDER BY orderid

;
-- HARD
-- 8. For all orders from previous question, show OrderDetails.
SELECT
FROM

;
-- HARD
-- 9. Get the list of all orders that are late. Ordered by delay.
SELECT
FROM

ORDER BY delay ASC

;
-- HARD
-- 10. Which salespeople has the most late orders?
SELECT
FROM

;
-- HARD
-- 11. For each EmployeeID show a number of AllOrders and LateOrders in one table.  
-- Show "0" if there is no LateOrders for Employee. (9 rows)
SELECT
FROM

;
-- HARD
-- 12. Add percentage of LateOrders column rounded by 0.01%
SELECT
FROM

;

