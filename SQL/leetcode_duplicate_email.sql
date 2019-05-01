# https://leetcode.com/problems/duplicate-emails

SELECT email 
FROM person
GROUP BY email
HAVING COUNT(email) > 1
;

# Alternate:
#SELECT p1.email
#FROM person p1
#INNER JOIN person p2
#  ON 
#    p1.email = p2.email
#    AND
#    p1.id <> p2.id
#GROUP BY p1.email
#;
