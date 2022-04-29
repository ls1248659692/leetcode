# Write your MySQL query statement below
SELECT d.name Department, e.name Employee, e.salary Salary
FROM Employee e
JOIN (SELECT id, salary, departmentId, DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) group_rank
FROM Employee) s ON s.id = e.id AND s.group_rank <= 3
LEFT JOIN Department d ON d.id = e.departmentId