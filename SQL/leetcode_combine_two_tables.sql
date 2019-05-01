# https://leetcode.com/problems/combine-two-tables/

SELECT firstname, lastname, address.city, address.state
FROM person
LEFT OUTER JOIN address
  ON person.personid = address.personid
;

