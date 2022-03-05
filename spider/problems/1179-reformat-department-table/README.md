# [Reformat Department Table][title]

## Description

部门表 `Department`：
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | id            | int     |    | revenue       | int     |    | month         | varchar |    +---------------+---------+    (id, month) 是表的联合主键。    这个表格有关于每个部门每月收入的信息。    月份（month）可以取下列值 ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]。    



编写一个 SQL 查询来重新格式化表，使得新的表中有一个部门 id 列和一些对应  **每个月** 的收入（revenue）列。

查询结果格式如下面的示例所示：
            Department 表：    +------+---------+-------+    | id   | revenue | month |    +------+---------+-------+    | 1    | 8000    | Jan   |    | 2    | 9000    | Jan   |    | 3    | 10000   | Feb   |    | 1    | 7000    | Feb   |    | 1    | 6000    | Mar   |    +------+---------+-------+        查询得到的结果表：    +------+-------------+-------------+-------------+-----+-------------+    | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |    +------+-------------+-------------+-------------+-----+-------------+    | 1    | 8000        | 7000        | 6000        | ... | null        |    | 2    | 9000        | null        | null        | ... | null        |    | 3    | null        | 10000       | null        | ... | null        |    +------+-------------+-------------+-------------+-----+-------------+        注意，结果表有 13 列 (1个部门 id 列 + 12个月份的收入列)。    


**Tags:** Database

**Difficulty:** Easy

## 思路

``` mysql
# Write your MySQL query statement below

SELECT DISTINCT d.id, m1.revenue AS Jan_Revenue, m2.revenue AS Feb_Revenue, m3.revenue AS Mar_Revenue, m4.revenue AS Apr_Revenue, m5.revenue AS May_Revenue, m6.revenue AS Jun_Revenue, m7.revenue AS Jul_Revenue, m8.revenue AS Aug_Revenue, m9.revenue AS Sep_Revenue, m10.revenue AS Oct_Revenue, m11.revenue AS Nov_Revenue, m12.revenue AS Dec_Revenue
FROM Department d
LEFT JOIN Department m1 ON m1.id = d.id AND m1.month = 'Jan'
LEFT JOIN Department m2 ON m2.id = d.id AND m2.month = 'Feb'
LEFT JOIN Department m3 ON m3.id = d.id AND m3.month = 'Mar'
LEFT JOIN Department m4 ON m4.id = d.id AND m4.month = 'Apr'
LEFT JOIN Department m5 ON m5.id = d.id AND m5.month = 'May'
LEFT JOIN Department m6 ON m6.id = d.id AND m6.month = 'Jun'
LEFT JOIN Department m7 ON m7.id = d.id AND m7.month = 'Jul'
LEFT JOIN Department m8 ON m8.id = d.id AND m8.month = 'Aug'
LEFT JOIN Department m9 ON m9.id = d.id AND m9.month = 'Sep'
LEFT JOIN Department m10 ON m10.id = d.id AND m10.month = 'Oct'
LEFT JOIN Department m11 ON m11.id = d.id AND m11.month = 'Nov'
LEFT JOIN Department m12 ON m12.id = d.id AND m12.month = 'Dec'
```

[title]: https://leetcode-cn.com/problems/reformat-department-table
