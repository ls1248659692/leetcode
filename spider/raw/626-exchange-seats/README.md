# [Exchange Seats][title]

## Description

表: `Seat`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | id          | int     |    | name        | varchar |    +-------------+---------+    Id是该表的主键列。    该表的每一行都表示学生的姓名和ID。    Id是一个连续的增量。    



编写SQL查询来交换每两个连续的学生的座位号。如果学生的数量是奇数，则最后一个学生的id不交换。

按 `id` **升序** 返回结果表。

查询结果格式如下所示。



**示例 1:**
            **输入:**     Seat 表:    +----+---------+    | id | student |    +----+---------+    | 1  | Abbot   |    | 2  | Doris   |    | 3  | Emerson |    | 4  | Green   |    | 5  | Jeames  |    +----+---------+    **输出:**     +----+---------+    | id | student |    +----+---------+    | 1  | Doris   |    | 2  | Abbot   |    | 3  | Green   |    | 4  | Emerson |    | 5  | Jeames  |    +----+---------+    **解释:** 请注意，如果学生人数为奇数，则不需要更换最后一名学生的座位。


**Tags:** Database

**Difficulty:** Medium

## 思路

``` mysql
# Write your MySQL query statement below

SELECT a.id, IFNULL(b.student, a.student) AS student
FROM Seat a
LEFT JOIN (SELECT IF(id % 2 = 0, id - 1, id + 1) AS id, student FROM Seat) b ON b.id = a.id
```

[title]: https://leetcode-cn.com/problems/exchange-seats
