-- EASY
-- 3. Return FirstName, LastName and HireDate fields for employees with the Title os "Sales 
-- Representative" from Employees table. (7 rows)
SELECT firstname, lastname, hiredate, title
FROM employees
WHERE LOWER(title) = LOWER('Sales Representative')
;
-- I used the LOWER() function here in case of variations in capitalization