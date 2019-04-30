-- EASY
-- 12.  Select FirstName, LastName for Employees and then create a new column 
-- FullName. Use space between words. (9 rows). Look online for examples of string 
-- concatenation in PostgreSQL and read about Aliases
SELECT firstname, lastname, CONCAT_WS(' ', firstname, lastname) AS FullName
FROM employees
;