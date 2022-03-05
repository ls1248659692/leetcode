# Write your MySQL query statement below
select b.id  from Weather a join Weather b on a.recordDate=Date_SUB(b.recordDate, interval 1 day) and a.temperature <b.temperature