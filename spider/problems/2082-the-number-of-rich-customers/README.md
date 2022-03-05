# [The Number of Rich Customers][title]

## Description

表： `Store`
            +-------------+------+    | Column Name | Type |    +-------------+------+    | bill_id     | int  |    | customer_id | int  |    | amount      | int  |    +-------------+------+    bill_id 是这个表的主键。    每一行包含一个订单的金额及相关客户的信息。    



写一条 SQL 语句，查询 **至少有一个** 订单的金额 **严格大于** `500` 的客户的数量。

查询结果格式如下示例所示：



**示例:**
            **输入：**    Store 表:    +---------+-------------+--------+    | bill_id | customer_id | amount |    +---------+-------------+--------+    | 6       | 1           | 549    |    | 8       | 1           | 834    |    | 4       | 2           | 394    |    | 11      | 3           | 657    |    | 13      | 3           | 257    |    +---------+-------------+--------+    **输出：**     +------------+    | rich_count |    +------------+    | 2          |    +------------+    **解释：**    客户 1 有 2 个订单金额严格大于 500。    客户 2 没有任何订单金额严格大于 500。    客户 3 有 1 个订单金额严格大于 500。    


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/the-number-of-rich-customers
