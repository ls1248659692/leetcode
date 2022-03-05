# [Triangle Judgement][title]

## Description

表: `Triangle`
            +-------------+------+    | Column Name | Type |    +-------------+------+    | x           | int  |    | y           | int  |    | z           | int  |    +-------------+------+    (x, y, z)是该表的主键列。    该表的每一行包含三个线段的长度。    



写一个SQL查询，每三个线段报告它们是否可以形成一个三角形。

以  **任意顺序  **返回结果表。

查询结果格式如下所示。



**示例 1:**
            **输入:**     Triangle 表:    +----+----+----+    | x  | y  | z  |    +----+----+----+    | 13 | 15 | 30 |    | 10 | 20 | 15 |    +----+----+----+    **输出:**     +----+----+----+----------+    | x  | y  | z  | triangle |    +----+----+----+----------+    | 13 | 15 | 30 | No       |    | 10 | 20 | 15 | Yes      |    +----+----+----+----------+


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/triangle-judgement
