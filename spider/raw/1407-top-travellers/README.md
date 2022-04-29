# [Top Travellers][title]

## Description

表：`Users`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | id            | int     |    | name          | varchar |    +---------------+---------+    id 是该表单主键。    name 是用户名字。

表：`Rides`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | id            | int     |    | user_id       | int     |    | distance      | int     |    +---------------+---------+    id 是该表单主键。    user_id 是本次行程的用户的 id, 而该用户此次行程距离为 distance 。    

写一段 SQL , 报告每个用户的旅行距离。

返回的结果表单，以 `travelled_distance` **降序排列** ，如果有两个或者更多的用户旅行了相同的距离, 那么再以 `name`
**升序排列** 。

查询结果格式如下例所示。
            Users 表：    +------+-----------+    | id   | name      |    +------+-----------+    | 1    | Alice     |    | 2    | Bob       |    | 3    | Alex      |    | 4    | Donald    |    | 7    | Lee       |    | 13   | Jonathan  |    | 19   | Elvis     |    +------+-----------+        Rides 表：    +------+----------+----------+    | id   | user_id  | distance |    +------+----------+----------+    | 1    | 1        | 120      |    | 2    | 2        | 317      |    | 3    | 3        | 222      |    | 4    | 7        | 100      |    | 5    | 13       | 312      |    | 6    | 19       | 50       |    | 7    | 7        | 120      |    | 8    | 19       | 400      |    | 9    | 7        | 230      |    +------+----------+----------+        Result 表：    +----------+--------------------+    | name     | travelled_distance |    +----------+--------------------+    | Elvis    | 450                |    | Lee      | 450                |    | Bob      | 317                |    | Jonathan | 312                |    | Alex     | 222                |    | Alice    | 120                |    | Donald   | 0                  |    +----------+--------------------+    Elvis 和 Lee 旅行了 450 英里，Elvis 是排名靠前的旅行者，因为他的名字在字母表上的排序比 Lee 更小。    Bob, Jonathan, Alex 和 Alice 只有一次行程，我们只按此次行程的全部距离对他们排序。    Donald 没有任何行程, 他的旅行距离为 0。    


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/top-travellers
