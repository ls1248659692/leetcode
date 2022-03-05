# [Managers with at Least 5 Direct Reports][title]

## Description

表: `Employee`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | id          | int     |    | name        | varchar |    | department  | varchar |    | managerId   | int     |    +-------------+---------+    Id是该表的主键列。    该表的每一行都表示雇员的名字、他们的部门和他们的经理的id。    如果managerId为空，则该员工没有经理。    没有员工会成为自己的管理者。    



编写一个SQL查询，查询 **至少有5名直接下属** 的经理 **** 。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。



**示例 1:**
            **输入:**     Employee 表:    +-----+-------+------------+-----------+    | id  | name  | department | managerId |    +-----+-------+------------+-----------+    | 101 | John  | A          | None      |    | 102 | Dan   | A          | 101       |    | 103 | James | A          | 101       |    | 104 | Amy   | A          | 101       |    | 105 | Anne  | A          | 101       |    | 106 | Ron   | B          | 101       |    +-----+-------+------------+-----------+    **输出:**     +------+    | name |    +------+    | John |    +------+


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/managers-with-at-least-5-direct-reports
