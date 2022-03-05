# Write your MySQL query statement below
select class from courses group by class having count(distinct student)>=5