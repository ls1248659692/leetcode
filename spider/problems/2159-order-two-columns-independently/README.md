# [Order Two Columns Independently][title]

## Description

Table: `Data`
            +-------------+------+    | Column Name | Type |    +-------------+------+    | first_col   | int  |    | second_col  | int  |    +-------------+------+    There is no primary key for this table and it may contain duplicates.    



Write an SQL query to independently:

  * order `first_col` in **ascending order**.
  * order `second_col` in **descending order**.

The query result format is in the following example.



**Example 1:**
            Input:     Data table:    +-----------+------------+    | first_col | second_col |    +-----------+------------+    | 4         | 2          |    | 2         | 3          |    | 3         | 1          |    | 1         | 4          |    +-----------+------------+    Output:     +-----------+------------+    | first_col | second_col |    +-----------+------------+    | 1         | 4          |    | 2         | 3          |    | 3         | 2          |    | 4         | 1          |    +-----------+------------+    


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/order-two-columns-independently
