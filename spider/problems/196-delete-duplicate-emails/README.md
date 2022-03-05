# [Delete Duplicate Emails][title]

## Description

表: `Person`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | id          | int     |    | email       | varchar |    +-------------+---------+    id是该表的主键列。    该表的每一行包含一封电子邮件。电子邮件将不包含大写字母。    



编写一个SQL查询来 **删除** 所有重复的电子邮件，只保留一个id最小的唯一电子邮件。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。



**示例 1:**
            **输入:**     Person 表:    +----+------------------+    | id | email            |    +----+------------------+    | 1  | john@example.com |    | 2  | bob@example.com  |    | 3  | john@example.com |    +----+------------------+    **输出:**     +----+------------------+    | id | email            |    +----+------------------+    | 1  | john@example.com |    | 2  | bob@example.com  |    +----+------------------+    **解释:** john@example.com重复两次。我们保留最小的Id = 1。


**Tags:** Database

**Difficulty:** Easy

## 思路

``` mysql
# Write your MySQL query statement below
delete from Person  where id not in( select mid from (select min(id) mid from Person group by Email)ta)
```

[title]: https://leetcode-cn.com/problems/delete-duplicate-emails
