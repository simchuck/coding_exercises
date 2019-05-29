# https://leetcode.com/problems/delete-duplicate-emails/

*** WIP ***

DELETE FROM person
WHERE (
    SELECT email 
    FROM person
    GROUP BY email
    HAVING COUNT(email) > 1
    ) 
