# [League Statistics][title]

## Description

Table: `Teams`
            +----------------+---------+    | Column Name    | Type    |    +----------------+---------+    | team_id        | int     |    | team_name      | varchar |    +----------------+---------+    team_id 是该表主键.    每一行都包含了一个参加联赛的队伍信息.    

Table: `Matches`
            +-----------------+---------+    | Column Name     | Type    |    +-----------------+---------+    | home_team_id    | int     |    | away_team_id    | int     |    | home_team_goals | int     |    | away_team_goals | int     |    +-----------------+---------+    (home_team_id, away_team_id) 是该表主键.    每一行包含了一次比赛信息.    home_team_goals 代表主场队得球数.    away_team_goals 代表客场队得球数.    获得球数较多的队伍为胜者队伍.    

写一段SQL，用来报告联赛信息. 统计数据应使用已进行的比赛来构建，其中获胜球队获得三分，而失败球队获得零分. 如果打平，两支球队都得一分.

result表的每行应包含以下信息:

  * `team_name` \- Teams表中的队伍名字
  * `matches_played` \- 主场与客场球队进行的比赛次数.
  * `points` \- 球队获得的总分数.
  * `goal_for` \- 球队在所有比赛中获取的总进球数
  * `goal_against` \- 球队在所有比赛中，他的对手球队的所有进球数
  * `goal_diff` \- `goal_for - goal_against`.

按分数降序返回结果表。 如果两队或多队得分相同，则按goal_diff 降序排列。 如果仍然存在平局，则以 team_name 按字典顺序排列它们。

查询的结果格式如下例所示:
            Teams table:    +---------+-----------+    | team_id | team_name |    +---------+-----------+    | 1       | Ajax      |    | 4       | Dortmund  |    | 6       | Arsenal   |    +---------+-----------+        Matches table:    +--------------+--------------+-----------------+-----------------+    | home_team_id | away_team_id | home_team_goals | away_team_goals |    +--------------+--------------+-----------------+-----------------+    | 1            | 4            | 0               | 1               |    | 1            | 6            | 3               | 3               |    | 4            | 1            | 5               | 2               |    | 6            | 1            | 0               | 0               |    +--------------+--------------+-----------------+-----------------+            Result table:    +-----------+----------------+--------+----------+--------------+-----------+    | team_name | matches_played | points | goal_for | goal_against | goal_diff |    +-----------+----------------+--------+----------+--------------+-----------+    | Dortmund  | 2              | 6      | 6        | 2            | 4         |    | Arsenal   | 2              | 2      | 3        | 3            | 0         |    | Ajax      | 4              | 2      | 5        | 9            | -4        |    +-----------+----------------+--------+----------+--------------+-----------+        Ajax (team_id=1) 有4场比赛: 2败2平. 总分数 = 0 + 0 + 1 + 1 = 2.    Dortmund (team_id=4) 有2场比赛: 2胜. 总分数 = 3 + 3 = 6.    Arsenal (team_id=6) 有2场比赛: 2平. 总分数 = 1 + 1 = 2.    Dortmund 是积分榜上的第一支球队. Ajax和Arsenal 有同样的分数, 但Arsenal的goal_diff高于Ajax, 所以Arsenal在表中的顺序在Ajaxzhi'qian.    


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/league-statistics
