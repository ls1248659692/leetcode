# Write your MySQL query statement below
select a.num  as ConsecutiveNums from Logs a join Logs b on a.num =b.num and a.id=b.id-1 join Logs c on a.num=c.num and a.id=c.id-2
group by a.num
