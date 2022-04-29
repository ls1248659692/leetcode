# Write your MySQL query statement below
select e.Name as Employee
from employee e
where salary > (select salary from employee where Id = e.ManagerId)