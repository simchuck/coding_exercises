# https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT e.name AS Employee
FROM employee e
JOIN employee m
  ON e.managerid = m.id
WHERE e.salary > m.salary
;

# The following version appears to be significantly faster...
SELECT e.name AS Employee
FROM employee e
JOIN employee m
  ON 
    e.managerid = m.id
    AND 
    e.salary > m.salary
;
