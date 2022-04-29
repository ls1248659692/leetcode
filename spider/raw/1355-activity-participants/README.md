# [Activity Participants][title]

## Description

表: `Friends`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | id            | int     |    | name          | varchar |    | activity      | varchar |    +---------------+---------+    id 是朋友的 id 和该表的主键    name 是朋友的名字    activity 是朋友参加的活动的名字    



表: `Activities`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | id            | int     |    | name          | varchar |    +---------------+---------+    id 是该表的主键    name 是活动的名字    



写一条 SQL 查询那些既没有最多，也没有最少参与者的活动的名字

`Activities` 表的每项活动的参与者都来自 Friends 表。

可以以 **任何顺序** 返回结果。

下面是查询结果格式的例子。



**示例 1:**
            **输入：**    Friends 表:    +------+--------------+---------------+    | id   | name         | activity      |    +------+--------------+---------------+    | 1    | Jonathan D.  | Eating        |    | 2    | Jade W.      | Singing       |    | 3    | Victor J.    | Singing       |    | 4    | Elvis Q.     | Eating        |    | 5    | Daniel A.    | Eating        |    | 6    | Bob B.       | Horse Riding  |    +------+--------------+---------------+    Activities 表:    +------+--------------+    | id   | name         |    +------+--------------+    | 1    | Eating       |    | 2    | Singing      |    | 3    | Horse Riding |    +------+--------------+    **输出：**    +--------------+    | activity     |    +--------------+    | Singing      |    +--------------+    **解释：**    Eating 活动有三个人参加, 是最多人参加的活动 (Jonathan D. , Elvis Q. and Daniel A.)    Horse Riding 活动有一个人参加, 是最少人参加的活动 (Bob B.)    Singing 活动有两个人参加 (Victor J. and Jade W.)


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/activity-participants
