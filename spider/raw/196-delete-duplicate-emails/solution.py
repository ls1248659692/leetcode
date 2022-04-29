# Write your MySQL query statement below
delete from Person  where id not in( select mid from (select min(id) mid from Person group by Email)ta)