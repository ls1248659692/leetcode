# [Highest Grade For Each Student][title]

## Description

表：`Enrollments`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | student_id    | int     |    | course_id     | int     |    | grade         | int     |    +---------------+---------+    (student_id, course_id) 是该表的主键。    



编写一个 SQL 查询，查询每位学生获得的最高成绩和它所对应的科目，若科目成绩并列，取 `course_id` 最小的一门。查询结果需按
`student_id` 增序进行排序。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。



**示例 1：**
            **输入：**    Enrollments 表：    +------------+-------------------+    | student_id | course_id | grade |    +------------+-----------+-------+    | 2          | 2         | 95    |    | 2          | 3         | 95    |    | 1          | 1         | 90    |    | 1          | 2         | 99    |    | 3          | 1         | 80    |    | 3          | 2         | 75    |    | 3          | 3         | 82    |    +------------+-----------+-------+    **输出：**    +------------+-------------------+    | student_id | course_id | grade |    +------------+-----------+-------+    | 1          | 2         | 99    |    | 2          | 2         | 95    |    | 3          | 3         | 82    |    +------------+-----------+-------+


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/highest-grade-for-each-student
