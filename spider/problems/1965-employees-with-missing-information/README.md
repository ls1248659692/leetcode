# [Employees With Missing Information][title]

## Description

表: `Employees`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | employee_id | int     |    | name        | varchar |    +-------------+---------+    employee_id 是这个表的主键。    每一行表示雇员的id 和他的姓名。    

表: `Salaries`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | employee_id | int     |    | salary      | int     |    +-------------+---------+    employee_id is 这个表的主键。    每一行表示雇员的id 和他的薪水。    

写出一个查询语句，找到所有丢失信息的雇员id。当满足下面一个条件时，就被认为是雇员的信息丢失：

  * 雇员的姓名丢失了，或者
  * 雇员的薪水信息丢失了，或者

返回这些雇员的id，从小到大排序。

查询结果格式如下面的例子所示：
            Employees table:    +-------------+----------+    | employee_id | name     |    +-------------+----------+    | 2           | Crew     |    | 4           | Haven    |    | 5           | Kristian |    +-------------+----------+    Salaries table:    +-------------+--------+    | employee_id | salary |    +-------------+--------+    | 5           | 76071  |    | 1           | 22517  |    | 4           | 63539  |    +-------------+--------+        Result table:    +-------------+    | employee_id |    +-------------+    | 1           |    | 2           |    +-------------+    雇员1，2，4，5 都工作在这个公司。        1号雇员的姓名丢失了。    2号雇员的薪水信息丢失了。    


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/employees-with-missing-information
