# [Convert Date Format][title]

## Description

表: `Days`
            +-------------+------+    | Column Name | Type |    +-------------+------+    | day         | date |    +-------------+------+    day 是这个表的主键。    

给定一个`Days`表，请你编写SQL查询语句，将`Days`表中的每一个日期转化为`"day_name, month_name day,
year"`格式的字符串。

返回的结果表不计顺序。

例如：
            Days table:    +------------+    | day        |    +------------+    | 2022-04-12 |    | 2021-08-09 |    | 2020-06-26 |    +------------+        Result table:    +-------------------------+    | day                     |    +-------------------------+    | Tuesday, April 12, 2022 |    | Monday, August 9, 2021  |    | Friday, June 26, 2020   |    +-------------------------+    请注意，输出对大小写敏感。    


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/convert-date-format
