# Write your MySQL query statement below

SELECT a.id, IFNULL(b.student, a.student) AS student
FROM Seat a
LEFT JOIN (SELECT IF(id % 2 = 0, id - 1, id + 1) AS id, student FROM Seat) b ON b.id = a.id