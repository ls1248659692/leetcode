# [Consecutive Numbers][title]

## Description

表：`Logs`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | id          | int     |    | num         | varchar |    +-------------+---------+    id 是这个表的主键。



编写一个 SQL 查询，查找所有至少连续出现三次的数字。

返回的结果表中的数据可以按 **任意顺序** 排列。

查询结果格式如下面的例子所示：



**示例 1:**
            **输入：**    Logs 表：    +----+-----+    | Id | Num |    +----+-----+    | 1  | 1   |    | 2  | 1   |    | 3  | 1   |    | 4  | 2   |    | 5  | 1   |    | 6  | 2   |    | 7  | 2   |    +----+-----+    **输出：**    Result 表：    +-----------------+    | ConsecutiveNums |    +-----------------+    | 1               |    +-----------------+    **解释：** 1 是唯一连续出现至少三次的数字。


**Tags:** Database

**Difficulty:** Medium

## 思路

``` mysql
# Write your MySQL query statement below
select a.num  as ConsecutiveNums from Logs a join Logs b on a.num =b.num and a.id=b.id-1 join Logs c on a.num=c.num and a.id=c.id-2
group by a.num

```

[title]: https://leetcode-cn.com/problems/consecutive-numbers
