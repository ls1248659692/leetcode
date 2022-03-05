# Write your MySQL query statement below

SELECT s.*
FROM Stadium s
LEFT JOIN Stadium sn2 ON sn2.id + 2 = s.id AND sn2.people >= 100
LEFT JOIN Stadium sn1 ON sn1.id + 1 = s.id AND sn1.people >= 100
LEFT JOIN Stadium s1 ON s1.id = s.id + 1 AND s1.people >= 100
LEFT JOIN Stadium s2 ON s2.id = s.id + 2 AND s2.people >= 100
WHERE s.people >= 100 AND
(((sn2.visit_date IS NOT NULL) AND (sn1.visit_date IS NOT NULL))
OR ((sn1.visit_date IS NOT NULL) AND (s1.visit_date IS NOT NULL))
OR ((s1.visit_date IS NOT NULL) AND (s2.visit_date IS NOT NULL)))