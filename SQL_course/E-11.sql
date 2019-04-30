-- EASY
-- 11. Select FirstName, LastName, Title and BirthDate for Employees ordered by 
-- BirthDate, but show only date for BirthDate without time.
SELECT firstname, lastname, title, DATE(birthdate)
FROM employees
ORDER BY birthdate ASC
;