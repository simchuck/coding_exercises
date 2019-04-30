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
