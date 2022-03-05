# Write your MySQL query statement below

SELECT d.name AS Department, e.name AS Employee, salary AS Salary
FROM Employee e
JOIN (SELECT departmentId, MAX(salary) m_s FROM Employee GROUP BY departmentId) ms ON e.departmentId = ms.departmentId AND e.salary = ms.m_s
LEFT JOIN Department d ON d.id = e.departmentId