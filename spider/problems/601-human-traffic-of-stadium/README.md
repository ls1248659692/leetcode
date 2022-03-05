# [Human Traffic of Stadium][title]

## Description

表：`Stadium`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | id            | int     |    | visit_date    | date    |    | people        | int     |    +---------------+---------+    visit_date 是表的主键    每日人流量信息被记录在这三列信息中： **序号** (id)、 **日期** (visit_date)、  **人流量** (people)    每天只有一行记录，日期随着 id 的增加而增加    



编写一个 SQL 查询以找出每行的人数大于或等于 `100` 且 `id` 连续的三行或更多行记录。

返回按 `visit_date` **升序排列** 的结果表。

查询结果格式如下所示。



**示例 1:**
            **输入：**    Stadium 表:    +------+------------+-----------+    | id   | visit_date | people    |    +------+------------+-----------+    | 1    | 2017-01-01 | 10        |    | 2    | 2017-01-02 | 109       |    | 3    | 2017-01-03 | 150       |    | 4    | 2017-01-04 | 99        |    | 5    | 2017-01-05 | 145       |    | 6    | 2017-01-06 | 1455      |    | 7    | 2017-01-07 | 199       |    | 8    | 2017-01-09 | 188       |    +------+------------+-----------+    **输出：**    +------+------------+-----------+    | id   | visit_date | people    |    +------+------------+-----------+    | 5    | 2017-01-05 | 145       |    | 6    | 2017-01-06 | 1455      |    | 7    | 2017-01-07 | 199       |    | 8    | 2017-01-09 | 188       |    +------+------------+-----------+    **解释：    id** 为 5、6、7、8 的四行 id 连续，并且每行都有 >= 100 的人数记录。    请注意，即使第 7 行和第 8 行的 visit_date 不是连续的，输出也应当包含第 8 行，因为我们只需要考虑 id 连续的记录。    不输出 id 为 2 和 3 的行，因为至少需要三条 id 连续的记录。


**Tags:** Database

**Difficulty:** Hard

## 思路

``` mysql
# Write your MySQL query statement below

SELECT s.*
FROM Stadium s
LEFT JOIN Stadium sn2 ON sn2.id + 2 = s.id AND sn2.people >= 100
LEFT JOIN Stadium sn1 ON sn1.id + 1 = s.id AND sn1.people >= 100
LEFT JOIN Stadium s1 ON s1.id = s.id + 1 AND s1.people >= 100
LEFT JOIN Stadium s2 ON s2.id = s.id + 2 AND s2.people >= 100
WHERE s.people >= 100 AND
(((sn2.visit_date IS NOT NULL) AND (sn1.visit_date IS NOT NULL))
OR ((sn1.visit_date IS NOT NULL) AND (s1.visit_date IS NOT NULL))
OR ((s1.visit_date IS NOT NULL) AND (s2.visit_date IS NOT NULL)))
```

[title]: https://leetcode-cn.com/problems/human-traffic-of-stadium
