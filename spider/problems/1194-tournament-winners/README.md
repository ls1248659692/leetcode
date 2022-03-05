# [Tournament Winners][title]

## Description

`Players` 玩家表
            +-------------+-------+    | Column Name | Type  |    +-------------+-------+    | player_id   | int   |    | group_id    | int   |    +-------------+-------+    player_id 是此表的主键。    此表的每一行表示每个玩家的组。    

`Matches` 赛事表
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | match_id      | int     |    | first_player  | int     |    | second_player | int     |     | first_score   | int     |    | second_score  | int     |    +---------------+---------+    match_id 是此表的主键。    每一行是一场比赛的记录，first_player 和 second_player 表示该场比赛的球员 ID。    first_score 和 second_score 分别表示 first_player 和 second_player 的得分。    你可以假设，在每一场比赛中，球员都属于同一组。    



每组的获胜者是在组内累积得分最高的选手。如果平局，`player_id` **最小  **的选手获胜。

编写一个 SQL 查询来查找每组中的获胜者。

返回的结果表单 **没有顺序要求**  。

查询结果格式如下所示。



**示例 1:**
            **输入：**    Players 表:    +-----------+------------+    | player_id | group_id   |    +-----------+------------+    | 15        | 1          |    | 25        | 1          |    | 30        | 1          |    | 45        | 1          |    | 10        | 2          |    | 35        | 2          |    | 50        | 2          |    | 20        | 3          |    | 40        | 3          |    +-----------+------------+    Matches 表:    +------------+--------------+---------------+-------------+--------------+    | match_id   | first_player | second_player | first_score | second_score |    +------------+--------------+---------------+-------------+--------------+    | 1          | 15           | 45            | 3           | 0            |    | 2          | 30           | 25            | 1           | 2            |    | 3          | 30           | 15            | 2           | 0            |    | 4          | 40           | 20            | 5           | 2            |    | 5          | 35           | 50            | 1           | 1            |    +------------+--------------+---------------+-------------+--------------+    **输出：**    +-----------+------------+    | group_id  | player_id  |    +-----------+------------+     | 1         | 15         |    | 2         | 35         |    | 3         | 40         |    +-----------+------------+


**Tags:** Database

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/tournament-winners
