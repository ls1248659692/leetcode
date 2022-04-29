# [Rank Scores][title]

## Description

表: `Scores`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | id          | int     |    | score       | decimal |    +-------------+---------+    Id是该表的主键。    该表的每一行都包含了一场比赛的分数。Score是一个有两位小数点的浮点值。    



编写 SQL 查询对分数进行排序。排名按以下规则计算:

  * 分数应按从高到低排列。
  * 如果两个分数相等，那么两个分数的排名应该相同。
  * 在排名相同的分数后，排名数应该是下一个连续的整数。换句话说，排名之间不应该有空缺的数字。

按 `score` 降序返回结果表。

查询结果格式如下所示。



**示例 1:**
            **输入:**     Scores 表:    +----+-------+    | id | score |    +----+-------+    | 1  | 3.50  |    | 2  | 3.65  |    | 3  | 4.00  |    | 4  | 3.85  |    | 5  | 4.00  |    | 6  | 3.65  |    +----+-------+    **输出:**     +-------+------+    | score | rank |    +-------+------+    | 4.00  | 1    |    | 4.00  | 1    |    | 3.85  | 2    |    | 3.65  | 3    |    | 3.65  | 3    |    | 3.50  | 4    |    +-------+------+


**Tags:** Database

**Difficulty:** Medium

## 思路

``` mysql
# Write your MySQL query statement below
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) 'rank'
FROM Scores
```

[title]: https://leetcode-cn.com/problems/rank-scores
