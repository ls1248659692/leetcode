# Write your MySQL query statement below
select p.Firstname, p.Lastname, a.City, a.State 
from Person p left join Address a on p.PersonId = a.PersonId