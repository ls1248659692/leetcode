# [The Change in Global Rankings][title]

## Description

Table: `TeamPoints`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | team_id     | int     |    | name        | varchar |    | points      | int     |    +-------------+---------+    team_id is the primary key for this table.    Each row of this table contains the ID of a national team, the name of the country it represents, and the points it has in the global rankings. No two teams will represent the same country.    



Table: `PointsChange`
            +---------------+------+    | Column Name   | Type |    +---------------+------+    | team_id       | int  |    | points_change | int  |    +---------------+------+    team_id is the primary key for this table.    Each row of this table contains the ID of a national team and the change in its points in the global rankings.    points_change can be:    - 0: indicates no change in points.    - positive: indicates an increase in points.    - negative: indicates a decrease in points.    Each team_id that appears in TeamPoints will also appear in this table.    



The **global ranking** of a national team is its rank after sorting all the
teams by their points **in descending order**. If two teams have the same
points, we break the tie by sorting them by their name **in lexicographical
order**.

The points of each national team should be updated based on its corresponding
`points_change` value.

Write an SQL query to calculate the change in the global rankings after
updating each team's points.

Return the result table in **any order**.

The query result format is in the following example.



**Example 1:**
            Input:     TeamPoints table:    +---------+-------------+--------+    | team_id | name        | points |    +---------+-------------+--------+    | 3       | Algeria     | 1431   |    | 1       | Senegal     | 2132   |    | 2       | New Zealand | 1402   |    | 4       | Croatia     | 1817   |    +---------+-------------+--------+    PointsChange table:    +---------+---------------+    | team_id | points_change |    +---------+---------------+    | 3       | 399           |    | 2       | 0             |    | 4       | 13            |    | 1       | -22           |    +---------+---------------+    Output:     +---------+-------------+-----------+    | team_id | name        | rank_diff |    +---------+-------------+-----------+    | 1       | Senegal     | 0         |    | 4       | Croatia     | -1        |    | 3       | Algeria     | 1         |    | 2       | New Zealand | 0         |    +---------+-------------+-----------+    Explanation:     The global rankings were as follows:    +---------+-------------+--------+------+    | team_id | name        | points | rank |    +---------+-------------+--------+------+    | 1       | Senegal     | 2132   | 1    |    | 4       | Croatia     | 1817   | 2    |    | 3       | Algeria     | 1431   | 3    |    | 2       | New Zealand | 1402   | 4    |    +---------+-------------+--------+------+    After updating the points of each team, the rankings became the following:    +---------+-------------+--------+------+    | team_id | name        | points | rank |    +---------+-------------+--------+------+    | 1       | Senegal     | 2110   | 1    |    | 3       | Algeria     | 1830   | 2    |    | 4       | Croatia     | 1830   | 3    |    | 2       | New Zealand | 1402   | 4    |    +---------+-------------+--------+------+    Since after updating the points Algeria and Croatia have the same points, they are ranked according to their lexicographic order.    Senegal lost 22 points but their rank did not change.    Croatia gained 13 points but their rank decreased by one.    Algeria gained 399 points and their rank increased by one.    New Zealand did not gain or lose points and their rank did not change.    


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/the-change-in-global-rankings
