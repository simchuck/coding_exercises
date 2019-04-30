-- EASY
-- 4. Return same fields for the same Title as in problem 3, but only for employees from the 
-- United States. (3 rows)
SELECT firstname, lastname, hiredate, title, country
FROM employees
WHERE LOWER(title) = LOWER('Sales Representative')
AND (country LIKE 'US%' OR country LIKE 'United States%')
;