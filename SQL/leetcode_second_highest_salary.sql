# https://leetcode.com/problems/second-highest-salary/

# Have to use the subquery (or something similar) to return a null when there is only one record.
SELECT
    (
    SELECT DISTINCT
        salary
    FROM 
        employee
    ORDER BY 
        salary DESC
    LIMIT 1
    OFFSET 1
    ) AS SecondHighestSalary
;

# This one seems even faster
#SELECT max(Salary) as SecondHighestSalary
#FROM Employee
#WHERE Salary < (SELECT max(Salary) FROM Employee)
#;

# I like where this next one is going, but there is an error in the `OFFSET` row...
#SELECT salary AS SecondHighestSalary
#FROM employee
#ORDER BY salary DESC
#OFFSET 1 ROWS
#FETCH NEXT 1 ROWS ONLY
#;

# Following fails when there is only one record, since it returns a non-null result
#SELECT salary AS SecondHighestSalary
#FROM (
#    SELECT salary FROM employee
#    ORDER BY salary DESC
#    LIMIT 2
#    ) toptwo
#ORDER BY salary ASC
#LIMIT 1
#;
