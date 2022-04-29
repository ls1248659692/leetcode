# [Shortest Distance in a Plane][title]

## Description

`Point2D` 表：
            +-------------+------+    | Column Name | Type |    +-------------+------+    | x           | int  |    | y           | int  |    +-------------+------+    (x, y) 是这张表的主键    这张表的每一行表示 X-Y 平面上一个点的位置    



`p1(x1, y1)` 和 `p2(x2, y2)` 这两点之间的距离是 `sqrt((x2 - x1)2 + (y2 - y1)2)` 。

请你写一个 SQL 查询报告 `Point2D` 表中任意两点之间的最短距离。保留 **2 位小数** 。

查询结果格式如下例所示。



**示例：**
            **输入：**    Point2D table:    +----+----+    | x  | y  |    +----+----+    | -1 | -1 |    | 0  | 0  |    | -1 | -2 |    +----+----+    **输出：**    +----------+    | shortest |    +----------+    | 1.00     |    +----------+    **解释：** 最短距离是 1.00 ，从点 (-1, -1) 到点 (-1, 2) 。    




**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/shortest-distance-in-a-plane
