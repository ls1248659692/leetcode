# [Primary Department for Each Employee][title]

## Description

Table: `Employee`
            +---------------+---------+    | Column Name   |  Type   |    +---------------+---------+    | employee_id   | int     |    | department_id | int     |    | primary_flag  | varchar |    +---------------+---------+    这张表的主键为 employee_id, department_id    employee_id 是员工的ID    department_id 是部门的ID，表示员工与该部门有关系    primary_flag 是一个枚举类型，值分别为('Y', 'N'). 如果值为'Y',表示该部门是员工的直属部门。 如果值是'N',则否    

一个员工可以属于多个部门。

当一个员工加入 **超过一个部门** 的时候，他需要决定哪个部门是他的直属部门。

请注意，当员工只加入一个部门的时候，那这个部门将默认为他的直属部门，虽然表记录的值为`'N'`.

请编写一段SQL，查出员工所属的直属部门。

返回结果没有顺序要求。

示例：
            Employee table:    +-------------+---------------+--------------+    | employee_id | department_id | primary_flag |    +-------------+---------------+--------------+    | 1           | 1             | N            |    | 2           | 1             | Y            |    | 2           | 2             | N            |    | 3           | 3             | N            |    | 4           | 2             | N            |    | 4           | 3             | Y            |    | 4           | 4             | N            |    +-------------+---------------+--------------+        Result table:    +-------------+---------------+    | employee_id | department_id |    +-------------+---------------+    | 1           | 1             |    | 2           | 1             |    | 3           | 3             |    | 4           | 3             |    +-------------+---------------+    - 员工1的直属部门是1    - 员工2的直属部门是1    - 员工3的直属部门是3    - 员工4的直属部门是3


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/primary-department-for-each-employee
