# [Fix Names in a Table][title]

## Description

表： `Users`
            +----------------+---------+    | Column Name    | Type    |    +----------------+---------+    | user_id        | int     |    | name           | varchar |    +----------------+---------+    user_id 是该表的主键。    该表包含用户的 ID 和名字。名字仅由小写和大写字符组成。    

编写一个 SQL 查询来修复名字，使得只有第一个字符是大写的，其余都是小写的。

返回按 `user_id` 排序的结果表。

查询结果格式示例如下：
            Users table:    +---------+-------+    | user_id | name  |    +---------+-------+    | 1       | aLice |    | 2       | bOB   |    +---------+-------+        Result table:    +---------+-------+    | user_id | name  |    +---------+-------+    | 1       | Alice |    | 2       | Bob   |    +---------+-------+    


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/fix-names-in-a-table
